# app.py
import streamlit as st

st.set_page_config(
    page_title="Portal Logística – Cadastros",
    page_icon="🧭",
    layout="wide"
)

# ====== CONFIGURE AQUI (SUBSTITUA PELAS SUAS URLs) ======
URL_WMS = "https://projetos-logistica.app.n8n.cloud/webhook/cadastro-usuarios"     # TODO: link GET do formulário de Cadastro de Usuário WMS
URL_LOCAL = "https://projetos-logistica.app.n8n.cloud/webhook/localizacao" # TODO: link GET do formulário de Cadastro de Localização
CONTATO_EMAIL = "projetos.logistica@somagrupo.com.br"
# =========================================================

# --- Estilo (cartões e botões) ---
st.markdown("""
<style>
:root{
  --bg:#f8fafc; --card:#ffffff; --text:#0f172a; --muted:#64748b;
  --accent:#1f2937; --ring:#2563eb; --shadow:0 10px 26px rgba(0,0,0,.08);
  --radius:18px;
}
.main > div { padding-top: 0 !important; }
h1, h2, h3 { letter-spacing:.2px }
.card{
  background:var(--card);
  border-radius:var(--radius);
  box-shadow:var(--shadow);
  padding:22px 22px 18px 22px;
  border:1px solid #e5e7eb;
  height:100%;
}
.kicker{ color:var(--muted); font-weight:600; font-size:.9rem; margin-bottom:6px }
.title{ font-weight:800; font-size:1.2rem; margin:0 0 6px }
.desc{ color:var(--muted); font-size:.95rem; margin:0 0 16px; line-height:1.45 }
a.linkbtn{
  display:inline-block; text-decoration:none; font-weight:700;
  background:var(--accent); color:white; padding:10px 14px;
  border-radius:12px; border:1px solid #0b1220; transition:transform .05s ease;
}
a.linkbtn:hover{ transform: translateY(-1px); }
.badge{
  display:inline-block; font-size:.78rem; padding:4px 8px; border-radius:999px;
  background:#eef2ff; color:#1e40af; border:1px solid #dbe3ff; margin-left:8px;
}
.footer{ color:var(--muted); font-size:.95rem; }
.footer a{ font-weight:700; color:#1e40af; text-decoration:none; }
.footer a:hover{ text-decoration:underline; }
hr{ border:none; border-top:1px solid #e5e7eb; margin:28px 0; }
</style>
""", unsafe_allow_html=True)

# --- Cabeçalho ---
st.markdown("### 🗂️ Portal de Cadastros – Logística")
st.markdown(
    "Selecione abaixo a ferramenta desejada. Os formulários abrem em uma nova aba."
)

st.markdown("---")

# --- Cards principais ---
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown(
        f"""
        <div class="card">
          <div class="kicker">Formulário</div>
          <p class="title">Cadastro de Usuário WMS</p>
          <p class="desc">
            Crie o usuário no padrão do WMS (turno, setor e regra de TC).
            A planilha e notificações são atualizadas automaticamente pelo fluxo do n8n.
          </p>
          <a class="linkbtn" href="{URL_WMS}" target="_blank" rel="noopener">
            Abrir formulário WMS
          </a>
          <span class="badge">on-line</span>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class="card">
          <div class="kicker">Formulário</div>
          <p class="title">Cadastro de Localização</p>
          <p class="desc">
            Solicite criação de endereços (PA/MP), com validação e preenchimento
            automático de colunas e prateleiras. Integra direto com a planilha.
          </p>
          <a class="linkbtn" href="{URL_LOCAL}" target="_blank" rel="noopener">
            Abrir formulário de Localização
          </a>
          <span class="badge">on-line</span>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

# --- Seção de contato ---
st.markdown("#### 📬 Fale com o time")
st.markdown(
    f"""
<div class="card">
  <p class="desc" style="margin:0">
    Dúvidas, erros ou melhorias? Fale com a equipe de Projetos de Logística.<br/>
    E-mail: <a href="mailto:{CONTATO_EMAIL}">{CONTATO_EMAIL}</a>
  </p>
</div>
""",
    unsafe_allow_html=True
)
