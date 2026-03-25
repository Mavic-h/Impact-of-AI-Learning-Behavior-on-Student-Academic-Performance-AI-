import json
from pathlib import Path

path = Path('final_project_student_ai_performance_analysis_bilingual_visual.ipynb')
nb = json.loads(path.read_text(encoding='utf-8'))

new_source = [
    "\n",
    "# -----------------------------\n",
    "# 6.3 Correlation heatmap | 相关性热力图\n",
    "# -----------------------------\n",
    "\n",
    "numeric_cols = data.select_dtypes(include=np.number).columns.tolist()\n",
    "corr_matrix = data[numeric_cols].corr()\n",
    "\n",
    "# Use a triangular view with circle markers to better show magnitude and direction\n",
    "mask = np.triu(np.ones_like(corr_matrix, dtype=bool))\n",
    "\n",
    "fig, ax = plt.subplots(figsize=(18, 12))\n",
    "sns.heatmap(\n",
    "    corr_matrix,\n",
    "    mask=mask,\n",
    "    cmap=\"coolwarm\",\n",
    "    center=0,\n",
    "    vmin=-1,\n",
    "    vmax=1,\n",
    "    cbar_kws={\"label\": \"Correlation coefficient\"},\n",
    "    square=True,\n",
    "    linewidths=0.5,\n",
    "    ax=ax,\n",
    "    annot=False,\n",
    ")\n",
    "\n",
    "# Overlay circles sized by abs(correlation) and annotate values\n",
    "for i in range(corr_matrix.shape[0]):\n",
    "    for j in range(corr_matrix.shape[1]):\n",
    "        if mask[i, j]:\n",
    "            continue\n",
    "        value = corr_matrix.iat[i, j]\n",
    "        size = np.abs(value) * 2500  # 调整圆点大小以获得更清晰的可视化\n",
    "        ax.scatter(\n",
    "            j + 0.5,\n",
    "            i + 0.5,\n",
    "            s=size,\n",
    "            c=[value],\n",
    "            cmap=\"coolwarm\",\n",
    "            vmin=-1,\n",
    "            vmax=1,\n",
    "            edgecolors=\"black\",\n",
    "            linewidths=0.5,\n",
    "            zorder=2,\n",
    "        )\n",
    "        ax.text(\n",
    "            j + 0.5,\n",
    "            i + 0.5,\n",
    "            f\"{value:.2f}\",\n",
    "            ha=\"center\",\n",
    "            va=\"center\",\n",
    "            fontsize=8,\n",
    "            zorder=3,\n",
    "        )\n",
    "\n",
    "ax.set_xticks(np.arange(len(corr_matrix.columns)) + 0.5)\n",
    "ax.set_yticks(np.arange(len(corr_matrix.columns)) + 0.5)\n",
    "ax.set_xticklabels(corr_matrix.columns, rotation=45, ha=\"right\")\n",
    "ax.set_yticklabels(corr_matrix.columns, rotation=0)\n",
    "ax.set_xlim(0, len(corr_matrix.columns))\n",
    "ax.set_ylim(len(corr_matrix.columns), 0)\n",
    "\n",
    "plt.title(\"Correlation Heatmap\", fontsize=14, fontweight='bold')\n",
    "plt.tight_layout()\n",
    "plt.show()\n",
]

updated = False
for cell in nb.get('cells', []):
    if cell.get('cell_type') == 'code':
        src = ''.join(cell.get('source', []))
        if '# 6.3 Correlation heatmap' in src:
            cell['source'] = new_source
            updated = True
            print('Updated correlation heatmap cell source (cell id:', cell.get('id'), ')')
            break

if not updated:
    raise RuntimeError('Failed to find the correlation heatmap cell to update')

path.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding='utf-8')
print('Notebook updated successfully.')
