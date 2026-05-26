import os
import subprocess

def generate_graph():
    # Dossier de destination (ton dossier Downloads visible sous Android)
    output_dir = os.path.expanduser("~/storage/downloads")
    dot_file = "diag_logique.dot"
    output_png = os.path.join(output_dir, "rendu_graphviz.png")

    # Exemple de contenu Graphviz si le fichier n'existe pas
    if not os.path.exists(dot_file):
        with open(dot_file, "w") as f:
            f.write('digraph G {\n  rankdir=LR;\n  "Entrée" -> "Analyse";\n  "Analyse" -> "Rendu";\n}')

    print(f"Génération du diagramme vers : {output_png}")
    
    try:
        # Exécution de la commande dot de Graphviz
        subprocess.run(["dot", "-Tpng", dot_file, "-o", output_png], check=True)
        print("✅ Rendu terminé avec succès !")
    except FileNotFoundError:
        print("❌ Erreur : Graphviz n'est pas installé. Tapez 'pkg install graphviz'.")
    except Exception as e:
        print(f"❌ Une erreur est survenue : {e}")

if __name__ == "__main__":
    generate_graph()
