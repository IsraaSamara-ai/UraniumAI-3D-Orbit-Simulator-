# app.py - التطبيق الرئيسي لمحاكاة توزيع إلكترونات اليورانيوم (بدون AI)
import streamlit as st
import numpy as np

# إعداد الصفحة
st.set_page_config(page_title="Uranium Atom Simulator", page_icon="⚛️", layout="wide")

# عنوان التطبيق
st.title("⚛️ **محاكاة التوزيع الإلكتروني لليورانيوم - UraniumAtom**")
st.markdown("""
<div style="text-align: center; color: #aaa;">
    ذرة اليورانيوم (U-92) | توزيع إلكتروني علمي: 2,8,18,32,21,9,2 | المستويات الفرعية: s, p, d, f
</div>
""", unsafe_allow_html=True)

# شريط جانبي للتحكم
st.sidebar.header("🎮 لوحة التحكم")
speed = st.sidebar.slider("سرعة الحركة", 0.5, 2.5, 1.0, 0.1)
st.sidebar.markdown("---")
st.sidebar.info("**المطور: Israa Samara**\n\nتصميم علمي دقيق يعرض الأغلفة K إلى Q والمستويات الفرعية.")

# إنشاء كود HTML/JS لعرض المجسم ثلاثي الأبعاد
def get_3d_html(speed_val):
    # التوزيع العلمي للإلكترونات في الأغلفة الرئيسية مع المستويات الفرعية
    shells = [
        {"name": "K", "radius": 1.8, "count": 2,  "color": 0x88aaff, "speedFactor": 1.0, "subshells": ["1s²"]},
        {"name": "L", "radius": 2.5, "count": 8,  "color": 0x99bbff, "speedFactor": 0.95, "subshells": ["2s²", "2p⁶"]},
        {"name": "M", "radius": 3.2, "count": 18, "color": 0xaaccff, "speedFactor": 0.90, "subshells": ["3s²", "3p⁶", "3d¹⁰"]},
        {"name": "N", "radius": 4.0, "count": 32, "color": 0xbbddff, "speedFactor": 0.85, "subshells": ["4s²", "4p⁶", "4d¹⁰", "4f¹⁴"]},
        {"name": "O", "radius": 4.8, "count": 21, "color": 0xcceeff, "speedFactor": 0.80, "subshells": ["5s²", "5p⁶", "5d¹⁰", "5f³"]},
        {"name": "P", "radius": 5.6, "count": 9,  "color": 0xddffff, "speedFactor": 0.75, "subshells": ["6s²", "6p⁶", "6d¹"]},
        {"name": "Q", "radius": 6.4, "count": 2,  "color": 0xeeffff, "speedFactor": 0.70, "subshells": ["7s²"]}
    ]
    
    import json
    shells_json = json.dumps(shells)
    
    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {{ margin: 0; overflow: hidden; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }}
            #info {{ position: absolute; top: 15px; left: 15px; color: white; background: rgba(0,0,0,0.7); padding: 8px 15px; border-radius: 8px; pointer-events: none; z-index: 10; font-size: 14px; }}
            #controls-note {{ position: absolute; bottom: 15px; left: 15px; color: rgba(255,255,255,0.5); background: rgba(0,0,0,0.5); padding: 4px 10px; border-radius: 5px; font-size: 12px; pointer-events: none; }}
        </style>
    </head>
    <body>
        <div id="info">
            <strong>⚛️ ذرة اليورانيوم (Uranium-92)</strong> | التوزيع الإلكتروني: 2,8,18,32,21,9,2 (K→Q)
        </div>
        <div id="controls-note">
            🖱️ تفاعل الماوس: سحب لتدوير | زر يمين لتحريك | عجلة لتكبير
        </div>

        <script type="importmap">
            {{
                "imports": {{
                    "three": "https://unpkg.com/three@0.128.0/build/three.module.js",
                    "three/addons/": "https://unpkg.com/three@0.128.0/examples/jsm/"
                }}
            }}
        </script>

        <script type="module">
            import * as THREE from 'three';
            import {{ OrbitControls }} from 'three/addons/controls/OrbitControls.js';
            import {{ CSS2DRenderer, CSS2DObject }} from 'three/addons/renderers/CSS2DRenderer.js';
            
            // إعداد المشهد
            const scene = new THREE.Scene();
            scene.background = new THREE.Color(0x050b1a);
            scene.fog = new THREE.FogExp2(0x050b1a, 0.008);
            
            const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.set(8, 5, 10);
            camera.lookAt(0, 0, 0);
            
            const renderer = new THREE.WebGLRenderer({{ antialias: true }});
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.shadowMap.enabled = true;
            document.body.appendChild(renderer.domElement);
            
            // معرض النصوص
            const labelRenderer = new CSS2DRenderer();
            labelRenderer.setSize(window.innerWidth, window.innerHeight);
            labelRenderer.domElement.style.position = 'absolute';
            labelRenderer.domElement.style.top = '0px';
            labelRenderer.domElement.style.left = '0px';
            labelRenderer.domElement.style.pointerEvents = 'none';
            document.body.appendChild(labelRenderer.domElement);
            
            // التحكم
            const controls = new OrbitControls(camera, renderer.domElement);
            controls.enableDamping = true;
            controls.dampingFactor = 0.05;
            controls.autoRotate = false;
            controls.enableZoom = true;
            controls.zoomSpeed = 1.2;
            
            // الإضاءة
            const ambientLight = new THREE.AmbientLight(0x404060);
            scene.add(ambientLight);
            const mainLight = new THREE.DirectionalLight(0xffffff, 1);
            mainLight.position.set(5, 10, 7);
            scene.add(mainLight);
            const backLight = new THREE.PointLight(0x3366cc, 0.5);
            backLight.position.set(-3, 2, -4);
            scene.add(backLight);
            const coreGlow = new THREE.PointLight(0xff6600, 0.8, 12);
            coreGlow.position.set(0, 0, 0);
            scene.add(coreGlow);
            
            // النواة
            const nucleusGeo = new THREE.SphereGeometry(0.7, 64, 64);
            const nucleusMat = new THREE.MeshStandardMaterial({{ color: 0xff5500, roughness: 0.3, metalness: 0.7, emissive: 0x442200 }});
            const nucleus = new THREE.Mesh(nucleusGeo, nucleusMat);
            nucleus.castShadow = true;
            scene.add(nucleus);
            
            // هالة
            const haloGeo = new THREE.SphereGeometry(0.9, 32, 32);
            const haloMat = new THREE.MeshBasicMaterial({{ color: 0xff8844, transparent: true, opacity: 0.2 }});
            const halo = new THREE.Mesh(haloGeo, haloMat);
            scene.add(halo);
            
            // بيانات الأغلفة من Python
            const shellsData = {shells_json};
            
            // إنشاء المدارات (الحلقات)
            shellsData.forEach(shell => {{
                const points = [];
                for (let ang = 0; ang <= 360; ang += 10) {{
                    const rad = ang * Math.PI / 180;
                    const x = shell.radius * Math.cos(rad);
                    const z = shell.radius * Math.sin(rad);
                    points.push(new THREE.Vector3(x, 0, z));
                }}
                const geometry = new THREE.BufferGeometry().setFromPoints(points);
                const material = new THREE.LineBasicMaterial({{ color: shell.color }});
                const orbit = new THREE.LineLoop(geometry, material);
                scene.add(orbit);
            }});
            
            // إضافة تسميات المستويات الفرعية
            shellsData.forEach(shell => {{
                const subshells = shell.subshells;
                const radius = shell.radius;
                const angles = [0, Math.PI/2, Math.PI, 3*Math.PI/2];
                for (let i = 0; i < subshells.length && i < angles.length; i++) {{
                    const angle = angles[i % angles.length];
                    const x = radius * 1.15 * Math.cos(angle);
                    const z = radius * 1.15 * Math.sin(angle);
                    const y = (i % 2 === 0 ? 0.4 : -0.4);
                    
                    const div = document.createElement('div');
                    div.textContent = subshells[i];
                    div.style.color = '#ffdd99';
                    div.style.fontSize = '13px';
                    div.style.fontWeight = 'bold';
                    div.style.backgroundColor = 'rgba(0,0,0,0.6)';
                    div.style.padding = '2px 6px';
                    div.style.borderRadius = '12px';
                    // التصحيح: استخدام ${{...}} لطباعة ${...} في الجافاسكريبت
                    div.style.border = `1px solid #${{shell.color.toString(16)}}`;
                    div.style.fontFamily = 'monospace';
                    
                    const label = new CSS2DObject(div);
                    label.position.set(x, y, z);
                    scene.add(label);
                }}
            }});
            
            // إنشاء الإلكترونات
            const electrons = [];
            shellsData.forEach(shell => {{
                const count = shell.count;
                const radius = shell.radius;
                const speedBase = shell.speedFactor;
                const color = shell.color;
                for (let i = 0; i < count; i++) {{
                    const angle = (i / count) * Math.PI * 2;
                    const speed = {speed_val} * speedBase * (1.2 / Math.sqrt(radius));
                    const electronGeo = new THREE.SphereGeometry(0.11, 32, 32);
                    const electronMat = new THREE.MeshStandardMaterial({{ 
                        color: color, 
                        emissive: 0x2266aa, 
                        emissiveIntensity: 0.3,
                        metalness: 0.1,
                        roughness: 0.4
                    }});
                    const electron = new THREE.Mesh(electronGeo, electronMat);
                    electron.userData = {{ radius, angle, speed }};
                    electron.position.x = radius * Math.cos(angle);
                    electron.position.z = radius * Math.sin(angle);
                    electron.position.y = 0;
                    scene.add(electron);
                    electrons.push(electron);
                }}
            }});
            
            // جسيمات الخلفية
            const particleCount = 800;
            const particleGeo = new THREE.BufferGeometry();
            const positions = new Float32Array(particleCount * 3);
            for (let i = 0; i < particleCount; i++) {{
                positions[i*3] = (Math.random() - 0.5) * 24;
                positions[i*3+1] = (Math.random() - 0.5) * 15;
                positions[i*3+2] = (Math.random() - 0.5) * 20 - 5;
            }}
            particleGeo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
            const particleMat = new THREE.PointsMaterial({{ color: 0x88aaff, size: 0.05, transparent: true, opacity: 0.4 }});
            const particles = new THREE.Points(particleGeo, particleMat);
            scene.add(particles);
            
            // حلقة الحركة
            function animate() {{
                requestAnimationFrame(animate);
                electrons.forEach(e => {{
                    e.userData.angle += 0.016 * e.userData.speed;
                    const x = Math.cos(e.userData.angle) * e.userData.radius;
                    const z = Math.sin(e.userData.angle) * e.userData.radius;
                    e.position.set(x, 0, z);
                    const intensity = 0.3 + Math.sin(e.userData.angle * 5) * 0.1;
                    e.material.emissiveIntensity = intensity;
                }});
                particles.rotation.y += 0.001;
                particles.rotation.x += 0.0005;
                const s = 1 + Math.sin(Date.now() * 0.004) * 0.03;
                halo.scale.set(s, s, s);
                coreGlow.intensity = 0.6 + Math.sin(Date.now() * 0.003) * 0.2;
                controls.update();
                renderer.render(scene, camera);
                labelRenderer.render(scene, camera);
            }}
            animate();
            
            window.addEventListener('resize', onWindowResize);
            function onWindowResize() {{
                camera.aspect = window.innerWidth / window.innerHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(window.innerWidth, window.innerHeight);
                labelRenderer.setSize(window.innerWidth, window.innerHeight);
            }}
        </script>
    </body>
    </html>
    """
    return html_code

# عرض المكون ثلاثي الأبعاد في Streamlit
final_html = get_3d_html(speed)
st.components.v1.html(final_html, height=700, scrolling=False)

# معلومات إضافية أسفل الصفحة
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("🔬 العدد الذري", "92")
with col2:
    st.metric("⚛️ الكتلة الذرية", "238.03 u")
with col3:
    st.metric("🌐 التوزيع الإلكتروني", "[Rn] 5f³ 6d¹ 7s²")