import streamlit as st

# ページ設定（スマートな外観を適用）
st.set_page_config(
    page_title="CORE-ANALYTICS // 期待値解析", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 漆黒とネオンを基調とした洗練されたカスタムCSS ---
st.markdown("""
    <style>
    /* 全体の背景とフォントの調整 */
    .main {
        background-color: #0d1117;
        color: #c9d1d9;
    }
    h1 {
        color: #ffffff;
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-weight: 800;
        letter-spacing: -0.5px;
        border-bottom: 2px solid #1f242c;
        padding-bottom: 10px;
    }
    h3 {
        color: #58a6ff !important;
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-top: 20px !important;
    }
    /* カードスタイルの枠組み */
    .stSelectbox, .stNumberInput {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 8px;
        padding: 12px;
        margin-bottom: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
    }
    /* 情報ボックスの高級化 */
    .stAlert {
        background-color: #1f242c !important;
        border: 1px solid #388bfd !important;
        border-radius: 8px !important;
        color: #58a6ff !important;
    }
    /* ブロック引用のプロ仕様化 */
    blockquote {
        background-color: #161b22 !important;
        border-left: 4px solid #8b949e !important;
        color: #8b949e !important;
        padding: 15px !important;
        border-radius: 0 8px 8px 0;
        font-size: 0.9rem;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

# タイトルセクション（近未来の解析端末をイメージ）
st.markdown("<h1>📊 CORE SYSTEM // データ解析端末</h1>", unsafe_allow_html=True)
st.caption("TARGET: AVIVA SHONANDAI / STADIUM FUTAMATAWAGAWA / PRESTO YAYOIDAI")

# --- データベース（各店の主軸・看板機種の4円等価ボーダー） ---
STORE_DATABASE = {
    "AVIVA湘南台店（1円パチンコ）": {
        "PA大海物語5 Withアグネス・ラム": {"prob": 99.9, "border_4k": 18.2, "type": "甘海"},
        "PAスーパー海物語 IN JAPAN2 金富士 99ver.": {"prob": 99.9, "border_4k": 17.7, "type": "甘海"},
        "P真・一騎当千～桃園の誓い～129ver.": {"prob": 129.7, "border_4k": 17.1, "type": "ライトミドル"},
        "P新世紀エヴァンゲリオン15 未来への咆哮 SPECIAL PREMIUM": {"prob": 129.8, "border_4k": 16.9, "type": "エヴァライト"},
    },
    "スタジアム二俣川店（1円パチンコ）": {
        "PAスーパー海物語IN沖縄6 Withえなこ": {"prob": 99.9, "border_4k": 17.3, "type": "甘海"},
        "PA新海物語": {"prob": 99.9, "border_4k": 18.5, "type": "甘海"},
        "P新世紀エヴァンゲリオン15 未来への咆哮 SPECIAL PREMIUM": {"prob": 129.8, "border_4k": 16.9, "type": "エヴァライト"},
        "Pフィーバー戦姫絶唱シンフォギア3 LIGHT ver.": {"prob": 99.1, "border_4k": 16.8, "type": "荒波甘"},
    },
    "プレスト弥生台店（2円パチンコ）": {
        "PA大海物語5 Withアグネス・ラム": {"prob": 99.9, "border_4k": 18.2, "type": "甘海"},
        "P真・一騎当千～桃園の誓い～129ver.": {"prob": 129.7, "border_4k": 17.1, "type": "ライトミドル"},
        "P新世紀エヴァンゲリオン15 未来への咆哮 SPECIAL PREMIUM": {"prob": 129.8, "border_4k": 16.9, "type": "エヴァライト"},
    }
}

# --- 1. ホール・機種選択 ---
st.markdown("### 🗺️ SECTION 01 // ホール・機種選択")
selected_store = st.selectbox("ロケーション選択", list(STORE_DATABASE.keys()))
is_2pachi = "2円" in selected_store

available_kishu = STORE_DATABASE[selected_store]
kishu_options = list(available_kishu.keys()) + ["【リストにない機種（自分でボーダーを入力する）】"]
selected_kishu = st.selectbox("ターゲット機種", kishu_options)

# スペックおよび等価ボーダー（4円換算値）の確定
if selected_kishu == "【リストにない機種（自分でボーダーを入力する）】":
    custom_border_4k = st.number_input("4円等価ボーダー（ネットの検索値を入力）", min_value=10.0, max_value=30.0, value=17.5, step=0.1)
    spec = {"prob": 99.9, "border_4k": custom_border_4k, "type": "カスタム"}
    display_name = "CUSTOM SPEC"
else:
    spec = available_kishu[selected_kishu]
    display_name = selected_kishu

# レートごとの損益分岐点の自動算出
if is_2pachi:
    target_border = round(spec["border_4k"] * 2.0, 1)
    unit_text = "500玉（1,000円）"
else:
    target_border = round(spec["border_4k"] * 4.0, 1)
    unit_text = "1,000玉（1,000円）"

st.info(f"📊 **{display_name}** 基準値\n目標ボーダー: **{unit_text} あたり {target_border} 回転以上**")

# --- 2. データランプからの生情報入力 ---
st.markdown("### 📈 SECTION 02 // 履歴データの同期")
col1, col2 = st.columns(2)
with col1:
    total_spin = st.number_input("本日の総回転数", min_value=0, max_value=9999, value=600, step=50)
with col2:
    bonus_count = st.number_input("総大当り回数", min_value=0, max_value=100, value=6, step=1)

# --- 3. 実際の釘（座ってからの体感）入力 ---
st.markdown("### 🎯 SECTION 03 // 実戦釘回りの入力")
if is_2pachi:
    actual_spin = st.number_input(f"実際の回転数 ／ 1,000円（500玉）あたり", min_value=10.0, max_value=80.0, value=35.0, step=0.5)
else:
    actual_spin = st.number_input(f"実際の回転数 ／ 1,000円（1,000玉）あたり", min_value=20.0, max_value=150.0, value=70.0, step=1.0)

# --- 解析アルゴリズム ---
st.write("---")
st.markdown("### ⚡ ANALYSIS // 期待値演算レポート")

# 前任者の粘り度（良釘推測）
history_factor = 0
if total_spin > 0:
    if total_spin >= 1200: history_factor += 20
    elif total_spin >= 600: history_factor += 10

spin_diff = actual_spin - target_border

score = 0
if is_2pachi:
    if spin_diff >= 2.0: score += 70
    elif spin_diff >= 0.5: score += 50
    elif spin_diff >= -0.5: score += 30
    else: score += 0
else:
    if spin_diff >= 4.0: score += 70
    elif spin_diff >= 1.0: score += 50
    elif spin_diff >= -1.0: score += 30
    else: score += 0

total_score = score + history_factor

# --- 視覚的に洗練された判定結果出力 ---
if total_score >= 80:
    st.markdown(f"""
        <div style="background: linear-gradient(135deg, #135200 0%, #092b00 100%); border: 2px solid #52c41a; padding: 20px; border-radius: 8px; color: #f6ffed;">
            <h2 style="margin: 0; color: #b7eb8f;">💎 判定: 超・お宝台（即確保）</h2>
            <p style="margin: 10px 0 0 0; font-size: 0.95rem; line-height: 1.5;">
                実戦値がボーダーを大幅超過。店側が明確にプラスに振っている極上の還元台です。<br>
                5,000円の投資上限を意識しつつ、1万円以上の利益奪取に向けて自信を持って全ツッパしてください！
            </p>
        </div>
    """, unsafe_allow_html=True)
    st.balloons()
elif total_score >= 60:
    st.markdown(f"""
        <div style="background: linear-gradient(135deg, #003a8c 0%, #002140 100%); border: 2px solid #1890ff; padding: 20px; border-radius: 8px; color: #e6f7ff;">
            <h2 style="margin: 0; color: #bae7ff;">📈 判定: 期待値プラス（勝負可能）</h2>
            <p style="margin: 10px 0 0 0; font-size: 0.95rem; line-height: 1.5;">
                打つほどにサイフが潤う優秀な調整です。無駄な粘りは排除しつつ、初当りからの一撃をスマートに狙いにいきましょう。
            </p>
        </div>
    """, unsafe_allow_html=True)
elif total_score >= 40:
    st.markdown(f"""
        <div style="background: linear-gradient(135deg, #ad6800 0%, #613b00 100%); border: 2px solid #faad14; padding: 20px; border-radius: 8px; color: #fffbe6;">
            <h2 style="margin: 0; color: #ffe58f;">⚠️ 判定: 様子見（投資は2,000円まで）</h2>
            <p style="margin: 10px 0 0 0; font-size: 0.95rem; line-height: 1.5;">
                ボーダー付近の並調整、または罠台の可能性があります。深追いは厳禁。<br>
                最初の2,000円で大当りを引き当てられなければ、即座に見切って移動を推奨します。
            </p>
        </div>
    """, unsafe_allow_html=True)
else:
    st.markdown(f"""
        <div style="background: linear-gradient(135deg, #a8071a 0%, #5c000b 100%); border: 2px solid #ff4d4f; padding: 20px; border-radius: 8px; color: #fff1f0;">
            <h2 style="margin: 0; color: #ffccc7;">🚨 判定: 危険・即退避（打つな！）</h2>
            <p style="margin: 10px 0 0 0; font-size: 0.95rem; line-height: 1.5;">
                圧倒的に回りが足りていません。この台への投資は、そのままお店への寄付行為になります。<br>
                1,000円分の検証が終わったなら、今すぐハンドルから手を離して撤退してください。
            </p>
        </div>
    """, unsafe_allow_html=True)

st.write("---")
st.markdown("### 🛠️ ANALYST NOTE")
st.blockquote("""
5,000円の投資で確実に1万円の純利を叩き出すための絶対条件。それは「罠台を最初の1,000円で見抜いて捨てる」という冷徹さだ。

前任者のヒキ強でデータランプがどれだけ華やかに見えても、SECTION 03の【実際の回転数】が基準値を下回った時点で、その台の期待値はマイナスだ。

この画面が叩き出す【超・お宝台】【期待値プラス】のサインのみを信じ、スマートかつ冷酷に立ち回ってくれ。データを制する者が、最後にホールを制する。
""")
