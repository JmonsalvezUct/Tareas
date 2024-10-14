import os
import shutil
import json

def crear_manifest_json(proyecto_dir, nombre_app, nombre_corto, descripcion):
    manifest = {
        "name": nombre_app,
        "short_name": nombre_corto,
        "description": descripcion,
        "start_url": "/index.html",
        "display": "standalone",
        "background_color": "#ffffff",
        "theme_color": "#000000",
        "icons": [
            {
                "src": "icon-192.png",
                "sizes": "192x192",
                "type": "image/png"
            },
            {
                "src": "icon-512.png",
                "sizes": "512x512",
                "type": "image/png"
            }
        ]
    }

    manifest_path = os.path.join(proyecto_dir, "manifest.json")
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=4)
    print(f"Archivo manifest.json creado en {manifest_path}")

def crear_sw_js(proyecto_dir):
    sw_content = '''
self.addEventListener('install', (e) => {
    e.waitUntil(
        caches.open('app-cache').then((cache) => {
            return cache.addAll([
                '/',
                '/index.html',
                '/sketch.js',
                '/icon-192.png',
                '/icon-512.png'
            ]);
        })
    );
});

self.addEventListener('fetch', (e) => {
    e.respondWith(
        caches.match(e.request).then((response) => {
            return response || fetch(e.request);
        })
    );
});
'''
    sw_path = os.path.join(proyecto_dir, "sw.js")
    with open(sw_path, "w") as f:
        f.write(sw_content)
    print(f"Archivo sw.js creado en {sw_path}")

def agregar_service_worker_al_index(proyecto_dir):
    index_path = os.path.join(proyecto_dir, "index.html")
    service_worker_script = '''
<script>
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js').then((registration) => {
            console.log('Service Worker registrado con éxito:', registration);
        }).catch((error) => {
            console.log('Service Worker fallo en el registro:', error);
        });
    });
}
</script>
'''
    if os.path.exists(index_path):
        with open(index_path, "a") as f:
            f.write(service_worker_script)
        print(f"Service Worker script añadido a {index_path}")
    else:
        print(f"Archivo {index_path} no encontrado")

def copiar_iconos(proyecto_dir):
    icono_192 = r"icon-192.png"
    icono_512 = r"icon-512.png"

    if os.path.exists(icono_192) and os.path.exists(icono_512):
        shutil.copy(icono_192, proyecto_dir)
        shutil.copy(icono_512, proyecto_dir)
        print(f"Iconos copiados hacia {proyecto_dir}")
    else:
        print("No se encontraron icon-192.png, icon-512.png")

def convertir_a_pwa(proyecto_dir, nombre_app, nombre_corto, descripcion):
    crear_manifest_json(proyecto_dir, nombre_app, nombre_corto, descripcion)
    crear_sw_js(proyecto_dir)
    agregar_service_worker_al_index(proyecto_dir)
    copiar_iconos(proyecto_dir)

if __name__ == "__main__":
    proyecto_dir = input("directorio de proyecto p5.js a convertir: ")

    if os.path.isdir(proyecto_dir):
        nombre_app   = input("Nombre largo de la Aplicación: ")
        nombre_corto = input("Nombre Corto de la Aplicación: ")
        descripcion  = input("Descripción breve  Aplicación: ")

        convertir_a_pwa(proyecto_dir, nombre_app, nombre_corto, descripcion)
    else:
        print(f"Carpeta {proyecto_dir} no existe")
