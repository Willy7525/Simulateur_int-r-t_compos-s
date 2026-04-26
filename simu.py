
import streamlit as st
import matplotlib.pyplot as plt

# Configuration de la page
st.set_page_config(page_title="Simulateur Bourse", page_icon="📈")

st.title("📈 Mon Simulateur d'Intérêts Composés")
st.write("Ce simulateur utilise ta logique de calcul (DCA en début de mois).")

# Barre latérale pour les entrées
with st.sidebar:
    st.header("Paramètres")
    v_initial = st.number_input("Capital Initial (€)", value=1000.0, step=100.0)
    dca = st.number_input("Versement Mensuel (DCA) (€)", value=200.0, step=10.0)
    taux_annuel = st.number_input("Rendement Annuel Espéré (%)", value=8.0, step=0.1)
    annees = st.number_input("Durée de l'investissement (Années)", value=20, step=1)

# Calculs (en gardant ta logique exacte)
interet_mensuel = taux_annuel / (12 * 100)
n_mois = annees * 12

vi = v_initial
historique_capital = [vi]
total_investi = v_initial
historique_investi = [total_investi]

for i in range(n_mois):
    # TA LOGIQUE : DCA d'abord, puis intérêts
    vi = vi + dca
    vi = vi * (1 + interet_mensuel)
    
    total_investi += dca
    
    historique_capital.append(vi)
    historique_investi.append(total_investi)

# Affichage des résultats principaux
col1, col2, col3 = st.columns(3)
col1.metric("Capital Final", f"{vi:,.0f} €")
col2.metric("Total Investi", f"{total_investi:,.0f} €")
col3.metric("Gain Intérêts", f"{vi - total_investi:,.0f} €")

# Graphique
st.subheader("Évolution du patrimoine")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(historique_capital, label="Valeur du portefeuille", color="#2ecc71", linewidth=2)
ax.fill_between(range(len(historique_capital)), historique_capital, color="#2ecc71", alpha=0.1)
ax.plot(historique_investi, label="Total des versements", color="#3498db", linestyle="--")

ax.set_xlabel("Mois")
ax.set_ylabel("Montant (€)")
ax.legend()
ax.grid(True, alpha=0.3)
st.pyplot(fig)