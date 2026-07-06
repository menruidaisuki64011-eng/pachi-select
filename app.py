import streamlit as st

# ページ設定
st.set_page_config(
    page_title="HYBRID-ANALYTICS // 総合解析端末", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- カスタムCSS（洗練されたダークサイバーな外観を維持） ---
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #c9d1d9; }
    h1 { color: #ffffff; font-family: Arial, sans-serif; font-weight: 800; border-bottom: 2px solid #1f242c; padding-bottom: 10px; }
    h3 { color: #58a6ff !important; font-size: 1.05rem !important; font-weight: 700 !important; letter-spacing: 0.5px; margin-top: 20px !important; }
    .stSelectbox, .stNumberInput { background-color: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 10px; margin-bottom: 5px; }
    .stAlert { background-color: #1f242c !important; border: 1px solid #388bfd !important; color: #58a6ff !important; border-radius: 8px !important; }
    blockquote { background-color: #161b22 !important; border-left: 4px solid #8b949e !important; color: #8b949e !important; padding: 15px !important; border-radius: 0 8px 8px 0; font-size: 0.9rem; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>🔮 HYBRID SYSTEM // 総合解析端末</h1>", unsafe_allow_html=True)
st.caption("現場の波感覚 と 科学的期待値 を融合した唯一無二の攻略デバイス")

# --- データベース ---
STORE_DATABASE = {
    "AVIVA湘南台店（1円パチンコ）": {
        "PA大海物語5 Withアグネス・ラム": {"border_4k": 18.2},
        "PAスーパー海物語 IN JAPAN2 金富士 99ver.": {"border_4k": 17.7},
        "P真・一騎当千～桃園の誓い～129ver.": {"border_4k": 17.1},
        "P新世紀エヴァンゲリオン15 未来への咆哮 SPECIAL PREMIUM": {"border_4k": 16.9},
    },
    "スタジアム二俣川店（1円パチンコ）": {
        "PAスーパー海物語IN沖縄6 Withえなこ": {"border_4k": 17.3},
        "PA新海物語": {"border_4k": 18.5},
        "P新世紀エヴァンゲリオン15 未来への咆哮 SPECIAL PREMIUM": {"border_4k": 16.9},
        "Pフィーバー戦姫絶唱シンフォギア3 LIGHT ver.": {"border_4k": 16.8},
    },
    "プレスト弥生台店（2円パチンコ）": {
        "PA大海物語5 Withアグネス・ラム": {"border_4k": 18.2},
        "P真・一騎当千～桃園の誓い～129ver.": {"border_4k": 17.1},
        "P新世紀エヴァンゲリオン15 未来への咆哮 SPECIAL PREMIUM": {"border_4k": 16.9},
    }
}

# --- 1. ホール・機種選択 ---
st.markdown("### 🗺️ SECTION 01 // ターゲット選択")
selected_store = st.selectbox("ロケーション選択", list(STORE_DATABASE.keys()))
is_2pachi = "2円" in selected_store

available_kishu = STORE_DATABASE[selected_store]
kishu_options = list(available_kishu.keys()) + ["【リストにない機種（自分でボーダーを入力する）】"]
selected_kishu = st.selectbox("ターゲット機種", kishu_options)

if selected_kishu == "【リストにない機種（自分でボーダーを入力する）】":
    custom_border_4k = st.number_input("4円等価ボーダー（ネットの検索値を入力）", min_value=10.0, max_value=30.0, value=17.5, step=0.1)
    border_4k = custom_border_4k
    display_name = "CUSTOM SPEC"
else:
    border_4k = available_kishu[selected_kishu]["border_4k"]
    display_name = selected_kishu

# レート換算ボーダーの計算
target_border = round(border_4k * (2.0 if is_2pachi else 4.0), 1)
unit_text = "500玉（1,000円）" if is_2pachi else "1,000玉（1,000円）"
st.info(f"📊 **{display_name}** ｜ 目標ボーダー: **{unit_text} あたり {target_border} 回転以上**")

# --- 2. 過去3日間のデータ履歴（ユーザー指定項目） ---
st.markdown("### 📊 SECTION 02 // 過去3日間の履歴同期")
st.caption("※データランプの数字をそのまま入力してください")

tab1, tab2, tab3 = st.tabs(["本日", "前日", "前々日"])
with tab1:
    today_spin = st.number_input("本日の総回転数", min_value=0, max_value=9999, value=300, step=50, key="t_spin")
    today_bonus = st.number_input("本日の総大当り回数", min_value=0, max_value=100, value=3, step=1, key="t_bonus")
with tab2:
    yest_spin = st.number_input("前日の総回転数", min_value=0, max_value=9999, value=800, step=50, key=\"y_spin\")
    yest_bonus = st.number_input("前日の総大当り回数", min_value=0, max_value=100, value=8, step=1, key=\"y_bonus\")
with tab3:
    day_before_spin = st.number_input("前々日の総回転数", min_value=0, max_value=9999, value=1200, step=50, key=\"db_spin\")
    day_before_bonus = st.number_input("前々日の総大当り回数", min_value=0, max_value=100, value=12, step=1, key=\"db_bonus\")

# --- 3. スランプグラフの波（ユーザー指定項目） ---
st.markdown("### 📈 SECTION 03 // スランプグラフの視認調整")
graph_trend = st.radio(
    "現在のスランプグラフの波の様子",
    ["📈 上がり調子（右肩上がり・好調波）", "📉 下がり調子（右肩下がり・ハマり波）", "↔️ 横ばい・変化なし"],
    index=2
)

# --- 4. 実際の釘（座ってからの体感）入力 ---
st.markdown("### 🎯 SECTION 04 // 実戦釘回りの入力")
st.caption("※座って最初の1,000円分を回した時点での、実際の回転数を入力します")
if is_2pachi:
    actual_spin = st.number_input(f"実際の回転数 ／ 1,000円（500玉）あたり", min_value=10.0, max_value=80.0, value=35.0, step=0.5)
else:
    actual_spin = st.number_input(f"実際の回転数 ／ 1,000円（1,000玉）あたり", min_value=20.0, max_value=150.0, value=70.0, step=1.0)

# --- ハイブリッド解析アルゴリズム ---
st.write("---")
st.markdown("### ⚡ ANALYZE // ハイブリッド演算レポート")

# ① 履歴と波によるメンタル補正・稼働良釘推測
bonus_score = 0
if graph_trend == "📈 上がり調子（右肩上がり・好調波）":
    bonus_score += 15
elif graph_trend == "📉 下がり調子（右肩下がり・ハマり波）":
    bonus_score -= 10

# 過去の総稼働が高ければ、店が開けている可能性アップ（プラス評価）
total_3day_spin = today_spin + yest_spin + day_before_spin
if total_3day_spin >= 2000:
    bonus_score += 10

# ② 実際の釘回り（期待値）の絶対評価
spin_diff = actual_spin - target_border
base_score = 0
if is_2pachi:
    if spin_diff >= 2.0: base_score += 70
    elif spin_diff >= 0.5: base_score += 50
    elif spin_diff >= -0.5: base_score += 30
else:
    if spin_diff >= 4.0: base_score += 70
    elif spin_diff >= 1.0: base_score += 50
    elif spin_diff >= -1.0: base_score += 30

# 総合点数の算出
total_score = base_score + bonus_score

# --- 結果出力 ---
if total_score >= 75:
    st.markdown(f"""
        <div style="background: linear-gradient(135deg, #135200 0%, #092b00 100%); border: 2px solid #52c41a; padding: 20px; border-radius: 8px; color: #f6ffed;">
            <h2 style="margin: 0; color: #b7eb8f;">💎 総合判定: 超・お宝台（即確保）</h2>
            <p style="margin: 10px 0 0 0; font-size: 0.95rem; line-height: 1.5;">
                過去の履歴・波の勢い、そして何より【実際の回り】がすべて最高水準で噛み合いました！<br>
                5,000円の投資上限を死守しつつ、1万円以上の利益奪取へ向けて強気に全ツッパしてください！
            </p>
        </div>
    """, unsafe_allow_html=True)
    st.balloons()
elif total_score >= 55:
    st.markdown(f"""
        <div style="background: linear-gradient(135deg, #003a8c 0%, #002140 100%); border: 2px solid #1890ff; padding: 20px; border-radius: 8px; color: #e6f7ff;">
            <h2 style="margin: 0; color: #bae7ff;">📈 総合判定: 期待値プラス（勝負可能）</h2>
            <p style="margin: 10px 0 0 0; font-size: 0.95rem; line-height: 1.5;">
                良好な台データと合格点の回りをマーク。十分にプラスを積み上げられる優秀台です。<br>
                5,000円制限のロックを意識しつつ、初当りからの一撃をもぎ取りにいきましょう。
            </p>
        </div>
    """, unsafe_allow_html=True)
elif total_score >= 35:
    st.markdown(f"""
        <div style="background: linear-gradient(135deg, #ad6800 0%, #613b00 100%); border: 2px solid #faad14; padding: 20px; border-radius: 8px; color: #fffbe6;">
            <h2 style="margin: 0; color: #ffe58f;">⚠️ 総合判定: 様子見（投資は2,000円まで！）</h2>
            <p style="margin: 10px 0 0 0; font-size: 0.95rem; line-height: 1.5;">
                データや波にやや不安があるか、回りの伸びが足りません。深追いは厳禁です。<br>
                最初の2,000円で大当りを射止められなければ、即座に見切って台を移動してください。
            </p>
        </div>
    """, unsafe_allow_html=True)
else:
    st.markdown(f"""
        <div style="background: linear-gradient(135deg, #a8071a 0%, #5c000b 100%); border: 2px solid #ff4d4f; padding: 20px; border-radius: 8px; color: #fff1f0;">
            <h2 style="margin: 0; color: #ffccc7;">🚨 総合判定: 危険・即退避（打つな！）</h2>
            <p style="margin: 10px 0 0 0; font-size: 0.95rem; line-height: 1.5;">
                回りがボーダーを大きく下回っているか、ハマり波に対して調整が死んでいます。<br>
                ここに命金を入れるのは極めて危険です。1,000円分の検証が終わったなら、即撤退してください。
            </p>
        </div>
    """, unsafe_allow_html=True)

st.write("---")
st.markdown("### 🛠️ ANALYST NOTE")
st.blockquote("""
現場で戦う人間の「直感とデータ」をすべて詰め込んだハイブリッド版だ。
過去3日間の流れ、そして今日の波の調子を脳内に同期させながら、最後の決定打として「実際の釘の回り」を叩き込む。

どんなに魅力的な波や履歴を描いていても、SECTION 04の【実際の回転数】が足りなければ、それはただの罠だ。逆に、波が良く、釘も開いている本物の還元台に出会ったとき、この画面は【超・お宝台】として最高の輝きを放つ。

5,000円投資で1万円を勝ぎ取る鉄の掟。自らの選んだデータを信じ、冷徹に立ち回ってくれ！
""")
