# ⚛️ UraniumAI-3D-Orbit-Simulator

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](رابط_تطبيقك_بعد_النشر)

## 🌟 وصف المشروع
**`UraniumAI-3D-Orbit-Simulator`** هو تطبيق ويب تفاعلي متقدم، يستخدم **الذكاء الاصطناعي** (Artificial Intelligence) للتنبؤ بحركة الإلكترونات حول نواة ذرة اليورانيوم (Uranium-92) في فضاء ثلاثي الأبعاد. تم بناء المشروع لتقديم تجربة تعليمية غامضة، حيث يمكن للمستخدمين التفاعل مع التوزيع الإلكتروني المعقد ومشاهدة مسارات الإلكترونات المتوقعة بواسطة نموذج **LSTM**.

### ✨ الميزات الرئيسية (Key Features)
*   **رسوم متحركة ثلاثية الأبعاد احترافية (High-End 3D Animation)**: تم إنشاؤها باستخدام مكتبة **Three.js** لعرض نواة اليورانيوم والإلكترونات في مداراتها.
*   **دمج الذكاء الاصطناعي للتنبؤ بالحركة (AI-Powered Motion Prediction)**: يستخدم نموذج **LSTM (Long Short-Term Memory)** تم تدريبه على بيانات حركة الإلكترونات للتنبؤ بمسارها المستقبلي وعرضه كمسار متقطع.
*   **واجهة مستخدم تفاعلية وجميلة (Beautiful Interactive UI)**: تم تطويرها باستخدام **Streamlit**، وتحتوي على أشرطة تحكم (Sidebar Controls) لتغيير سرعة المحاكاة وعدد الإلكترونات المعروضة.
*   **قابل للنشر على GitHub وStreamlit Cloud**: يمكن نشره بسهولة ليكون متاحاً للجميع عبر متصفح الويب.
*   **تفاعل مباشر**: يمكن للمستخدم النقر والسحب على الشاشة لتدوير المجسم ثلاثي الأبعاد وتكبير/تصغيره (Zoom/Pan) لمشاهدته من جميع الزوايا.

### 🛠️ التقنيات المستخدمة (Tech Stack)
*   **الواجهة الأمامية والخادم (Frontend & Backend)**: Python, Streamlit
*   **الرسومات ثلاثية الأبعاد (3D Graphics)**: Three.js (ضمن مكون `st.components.v1.html`)
*   **الذكاء الاصطناعي (AI)**: TensorFlow / Keras (لإنشاء نموذج LSTM)
*   **الحوسبة العلمية (Scientific Computing)**: NumPy
*   **النشر (Deployment)**: Streamlit Community Cloud (أو Hugging Face Spaces, Render)

### 🚀 كيفية التشغيل محلياً (Local Setup)
1.  انسخ المستودع (Clone the repository):
    ```bash
    git clone https://github.com/IsraaSamara/UraniumAI-3D-Orbit-Simulator.git
    cd UraniumAI-3D-Orbit-Simulator