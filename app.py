import streamlit as st

st.set_page_config(
    page_title="Dos de Agosto",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Plus+Jakarta+Sans:wght@300;400;600&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Plus Jakarta Sans', sans-serif;
            color: #1a1a1a;
            background-color: #faf9f6;
        }
            
        h1, h2, h3 {
            font-family: 'Playfair Display', serif !important;
            font-weight: 600 !important;
            letter-spacing: -0.5px;
        }
            
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
            
        .book-card {
            background-color: #ffffff;
            border: 1px solid #e5e5e5;
            border-radius: 8px;
            padding: 24px;
            margin-bottom: 20px;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
            
        .book-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.5);
        }
                        
        .badge {
            display: inline-block;
            background-color: #1a1a1a;
            color: white;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 12px;
        }
            
        .quote-box {
            border-left: 2px solid #1a1a1a;
            padding-left: 16px;
            font-style: italic;
            color: #555;
            margin: 16px 0;
        }
        </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; font-size: 3rem; margin-top: 1rem;'>CAFÉ & LETRAS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic; color: #666;'>Club de lectura de Claudia, Irene y Andrea</p>", unsafe_allow_html=True)
st.markdown("---")

tab1, tab2, tab3, tab4 = st.tabs(["📖 Libro del mes", "📚 Biblioteca", "💡 Guía de debate", "💬 Comunidad"])

with tab1:
    col_img, col_info = st.columns([1, 2], gap="large")

    # portada del libro
    with col_img:
        st.image(
            "https://images.unsplash.com/photo-1544947950-fa07a98d237f?auto=format&fit=crop&q=80&w=800",
            use_container_width=True,
            caption="Selección del mes"
        )

    with col_info:
        st.markdown("<span class='badge'>Lectura actual - Agosto</span>", unsafe_allow_html=True)
        st.markdown("## Título del libro")
        st.markdown("<b>Autor:</b> Nombre del autor | <b>Páginas:</b> Número de páginas | <b>Género:</b> Género del libro")

        st.write("""
        Descripción del libro + por qué se escogió para este mes.
        """)

        st.markdown("""
        <div class="quote-box">
            "Alguna frase del libro."
        </div>
        """, unsafe_allow_html=True)

        st.info("📅 <b>Próxima reunión:</b> Fecha y hora | 📍 <b>Lugar:</b> Casa de Claudia")

with tab2:
    st.markdown("### Histórico de lecturas")
    st.write("Libros que hemos leído:")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="book-card">
            <span style="color:#888; font-size: 0.85rem;">Mes y año de lectura</span>
            <h3>Título del libro</h3>
            <p><b>Autor: Nombre del autor</b> - ⭐ Puntuación / 5</p>
            <p>Sinopsis del libro</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="book-card">
            <span style="color:#888; font-size: 0.85rem;">Mes y año de lectura</span>
            <h3>Título del libro</h3>
            <p><b>Autor: Nombre del autor</b> - ⭐ Puntuación / 5</p>
            <p>Sinopsis del libro</p>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    st.markdown("### Preguntas para el debate del mes")
    
    with st.expander("Capítulos x al y"):
        st.write("Pregunta 1")
        st.write("Pregunta 2")

    with st.expander("Capítulos y+1 al z"):
        st.write("Pregunta 1")
        st.write("Pregunta 2")

with tab4:
    col_prop, col_rsvp = st.columns(2, gap="large")

    with col_prop:
        st.markdown("### Proponer lectura")
        with st.form("proponer_libro"):
            title = st.text_input("Título del libro")
            author = st.text_input("Autor del libro")
            reason = st.text_area("¿Por qué deberíamos leerlo?")
            submit_button = st.form_submit_button("Enviar propuesta")

            if submit_button:
                st.success(f"{title} ha sido añadido a la lista de candidatos.")
    
    with col_rsvp:
        st.markdown("### Confirmar asistencia")
        name = st.text_input("Nombre")
        attendance = st.radio("¿Asistirás a la próxima reunión?", ("Sí", "No"))
        
        if st.button("Confirmar"):
            st.balloons()
            st.success(f"Confirmación guardada para {name}.")