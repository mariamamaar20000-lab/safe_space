system_prompt = f"""
أنت Dr. Sharon
دكتور نفسي رجل
بتتكلم مصري طبيعي جدًا
كلامك بسيط، واقعي، مش فيك
بتسأل بس لما السؤال مهم
أحيانًا تسكت لو السكوت أحسن
بتفتكر الأنماط مش الكلام
ما بتحكمش
ما تديش حلول جاهزة
خليك بني آدم قبل ما تكون دكتور
الحالة النفسية: {state}
مستوى الخطر: {risk}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_text}
        ],
        temperature=0.9
    )

    return response.choices[0].message.content, traits, score, exercise, memory_note

# ================= CHAT VIEW =================
for m in st.session_state.chat:
    css = "alert" if m.get("alert") else ("user" if m["role"]=="user" else "bot")
    name = "أنت" if m["role"]=="user" else "د. شارون"
    st.markdown(
        f'<div class="box {css}"><b>{name}:</b> {m["text"]}<br><span class="small">{m.get("meta","")}</span></div>',
        unsafe_allow_html=True
    )

# ================= INPUT =================
with st.form("input", clear_on_submit=True):
    text = st.text_input("اتكلم… كل اللي جواك آمن هنا")
    send = st.form_submit_button("إرسال")

if send and text:
    state, risk = psycho_scan(text)
    reply, traits, score, exercise, memory_note = dr_sharon_ai(text, state, risk)

    st.session_state.chat.append({
        "role":"user",
        "text":text,
        "meta":f"🧠 الحالة: {state} | ⚠️ الخطر: {risk}"
    })

    st.session_state.chat.append({
        "role":"bot",
        "text":reply,
        "meta":f"📊 تحليل: {state} | 🧬 سمات: {', '.join(traits)} | 📈 المؤشر: {score}/100 | 🧘 تمرين: {exercise}\n{memory_note}",
        "alert": True if "HIGH" in risk else False
    })

    st.rerun()

# ================= RESET =================
if st.button("🗑️ جلسة جديدة"):
    st.session_state.chat = []
    st.session_state.patterns = []
    st.rerun()
