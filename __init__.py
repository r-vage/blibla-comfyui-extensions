import os
import nodes
"""
import shutil

comfy_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
failfast_path = os.path.abspath(os.path.dirname(__file__))

def setup_js():
    try:
        js_dest_path = os.path.join(comfy_path, "web", "extensions",  "failfast-comfyui-extensions")
        js_src_path = os.path.join(failfast_path, "extensions")
        print(js_src_path)
        print(js_dest_path)
        if os.path.exists(js_dest_path):
            shutil.rmtree(js_dest_path)

        shutil.copytree(js_src_path, js_dest_path)
        
    except Exception as e:
        print(f"An error occurred: {e}")

setup_js()
"""
nodes.EXTENSION_WEB_DIRS["blibla-comfyui-extensions"] = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "extensions"
)
NODE_CLASS_MAPPINGS = {}
