import streamlit as st

st.set_page_config(
    page_title="🐴 Feed the Herd 🥕",
    page_icon="🐴",
    layout="wide",
    initial_sidebar_state="collapsed",
)

GAME_URL = "https://iremhamurcuoglu.github.io/hungry_herd_irem/"

# Full page game embed with keyboard focus fix
st.markdown(f"""
<style>
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    .block-container {{
        padding: 0 !important;
        max-width: 100% !important;
    }}
    .stApp {{
        background: #1a1a2e;
        overflow: hidden;
    }}
    .game-wrapper {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;
        min-height: 95vh;
        background: #1a1a2e;
    }}
    .game-title {{
        color: #ffd700;
        font-family: Arial, sans-serif;
        font-size: 22px;
        margin-bottom: 6px;
    }}
    .game-info {{
        color: #888;
        font-family: Arial, sans-serif;
        font-size: 13px;
        margin-bottom: 10px;
    }}
    #game-frame {{
        border: 2px solid #333;
        border-radius: 8px;
        background: #000;
    }}
</style>

<div class="game-wrapper">
    <div class="game-title">🐴 Feed the Herd 🥕</div>
    <div class="game-info">Oyuna tıklayarak focus verin. Tıklama ile hareket, butonlar ile aksiyon.</div>
    <iframe id="game-frame"
        src="{GAME_URL}"
        width="1024" height="768"
        scrolling="no"
        allow="autoplay; fullscreen; gamepad"
        allowfullscreen
        tabindex="0"
    ></iframe>
</div>

<script>
// iframe'e otomatik focus ver
(function() {{
    function focusGame() {{
        var frame = document.getElementById('game-frame');
        if (frame) {{
            frame.focus();
        }}
    }}
    // Sayfa yüklendiğinde
    setTimeout(focusGame, 1000);
    setTimeout(focusGame, 3000);

    // iframe'e tıklayınca focus ver
    document.addEventListener('click', function(e) {{
        var frame = document.getElementById('game-frame');
        if (frame) frame.focus();
    }});

    // Yön tuşları ve Space'in sayfayı kaydırmasını engelle
    document.addEventListener('keydown', function(e) {{
        if (['ArrowUp','ArrowDown','ArrowLeft','ArrowRight','Space',' '].indexOf(e.key) !== -1) {{
            e.preventDefault();
            // iframe'e focus ver
            var frame = document.getElementById('game-frame');
            if (frame) frame.focus();
        }}
    }}, {{passive: false}});
}})();
</script>
""", unsafe_allow_html=True)
