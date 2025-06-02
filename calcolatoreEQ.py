import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib
matplotlib.use('TkAgg')

class CalcolatoreEquilibrioMercato:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calcolatore Equilibrio di Mercato")
        
        self.configura_stile()
        
        self.root.configure(bg='#282c34')
        padding = 20
        self.root.geometry("1200x800")
        
        contenitore_principale = ttk.Frame(self.root, padding=f"{padding}", style="Main.TFrame")
        contenitore_principale.grid(row=0, column=0, sticky="nsew")
        
        self.crea_sezione_input(contenitore_principale)
        self.crea_sezione_grafico(contenitore_principale)
        self.crea_sezione_risultati(contenitore_principale)
        
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        contenitore_principale.grid_columnconfigure(1, weight=1)
        contenitore_principale.grid_rowconfigure(0, weight=1)

    def configura_stile(self):
        stile = ttk.Style()
        
        colore_sfondo = '#282c34'
        colore_testo = '#abb2bf'
        colore_accento = '#61afef'
        sfondo_secondario = '#21252b'
        pulsante_hover = '#528bff'
        
        stile.theme_use('clam')
        
        stile.configure("Main.TFrame",
            background=colore_sfondo,
            relief="flat",
            borderwidth=0
        )
        
        stile.configure(".",
            background=colore_sfondo,
            foreground=colore_testo,
            font=("JetBrains Mono", 10),
            fieldbackground=sfondo_secondario,
            selectbackground=colore_accento,
            selectforeground='white'
        )
        
        stile.configure("Custom.TLabelframe", 
            background=colore_sfondo,
            foreground=colore_testo,
            bordercolor=colore_accento,
            borderwidth=2,
            relief="solid",
            lightcolor=colore_sfondo,
            darkcolor=colore_sfondo
        )
        
        stile.configure("Custom.TLabelframe.Label", 
            background=colore_sfondo,
            foreground=colore_accento,
            font=("JetBrains Mono", 12, "bold")
        )
        
        stile.configure("Inner.TFrame",
            background=colore_sfondo,
            relief="flat",
            borderwidth=0
        )
        
        stile.configure("Parameter.TLabel",
            background=colore_sfondo,
            foreground=colore_accento,
            font=("JetBrains Mono", 10, "bold")
        )
        
        stile.configure("Custom.TButton",
            background=colore_accento,
            foreground='white',
            padding=(40, 15),
            font=("JetBrains Mono", 11, "bold"),
            borderwidth=0,
            relief="flat",
            focuscolor='none'
        )
        
        stile.map("Custom.TButton",
            background=[
                ("pressed", pulsante_hover),
                ("active", pulsante_hover)
            ],
            foreground=[
                ("pressed", "white"),
                ("active", "white")
            ],
            relief=[("pressed", "flat"), ("active", "flat")]
        )
        
        stile.configure("Custom.TLabel",
            background=colore_sfondo,
            foreground=colore_testo,
            font=("JetBrains Mono", 10)
        )
        
        stile.configure("Bold.TLabel",
            background=colore_sfondo,
            foreground=colore_testo,
            font=("JetBrains Mono", 11, "bold")
        )
        
        stile.configure("Success.TLabel",
            background=colore_sfondo,
            foreground="#98c379",
            font=("JetBrains Mono", 10, "bold")
        )
        
        stile.configure("Error.TLabel",
            background=colore_sfondo,
            foreground="#e06c75",
            font=("JetBrains Mono", 10, "bold")
        )
        
        stile.configure("Custom.TEntry",
            fieldbackground=sfondo_secondario,
            foreground=colore_testo,
            bordercolor=colore_accento,
            insertcolor=colore_testo,
            relief="solid",
            borderwidth=1,
            padding=8
        )
        
        stile.map("Custom.TEntry",
            focuscolor=[("focus", colore_accento)],
            bordercolor=[("focus", colore_accento)]
        )
        
        stile.configure("Custom.TSeparator",
            background=colore_accento
        )

    def crea_sezione_input(self, genitore):
        sezione_input = ttk.LabelFrame(
            genitore, 
            text="Parametri", 
            style="Custom.TLabelframe",
            padding="20"
        )
        sezione_input.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        ttk.Label(sezione_input, text="Curva di Offerta: p = a·q² + b", 
                 style="Bold.TLabel").pack(anchor='w', pady=(10,5))
        
        frame_parametri_offerta = ttk.Frame(sezione_input, style="Inner.TFrame")
        frame_parametri_offerta.pack(fill='x', pady=5)
        
        ttk.Label(frame_parametri_offerta, text="a:", style="Parameter.TLabel").pack(side='left')
        self.campo_a = ttk.Entry(frame_parametri_offerta, width=10, style='Custom.TEntry')
        self.campo_a.pack(side='left', padx=5)
        
        ttk.Label(frame_parametri_offerta, text="b:", style="Parameter.TLabel").pack(side='left', padx=(10,0))
        self.campo_b = ttk.Entry(frame_parametri_offerta, width=10, style='Custom.TEntry')
        self.campo_b.pack(side='left', padx=5)
        
        ttk.Label(sezione_input, text="Curva di Domanda: q = c - d·p", 
                 style="Bold.TLabel").pack(anchor='w', pady=(20,5))
        
        frame_parametri_domanda = ttk.Frame(sezione_input, style="Inner.TFrame")
        frame_parametri_domanda.pack(fill='x', pady=5)
        
        ttk.Label(frame_parametri_domanda, text="c:", style="Parameter.TLabel").pack(side='left')
        self.campo_c = ttk.Entry(frame_parametri_domanda, width=10, style='Custom.TEntry')
        self.campo_c.pack(side='left', padx=5)
        
        ttk.Label(frame_parametri_domanda, text="d:", style="Parameter.TLabel").pack(side='left', padx=(10,0))
        self.campo_d = ttk.Entry(frame_parametri_domanda, width=10, style='Custom.TEntry')
        self.campo_d.pack(side='left', padx=5)
        
        frame_pulsante = ttk.Frame(sezione_input, style="Inner.TFrame")
        frame_pulsante.pack(pady=(30,20))
        
        self.pulsante_calcola = ttk.Button(
            frame_pulsante, 
            text="Calcola Equilibrio", 
            command=self.calcola_equilibrio, 
            style="Custom.TButton"
        )
        self.pulsante_calcola.pack()
        
    def crea_sezione_grafico(self, genitore):
        sezione_grafico = ttk.LabelFrame(
            genitore, 
            text="Grafico", 
            style="Custom.TLabelframe",
            padding="10"
        )
        sezione_grafico.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")
        
        self.figura = plt.Figure(figsize=(8, 6), dpi=100)
        self.grafico = self.figura.add_subplot(111)
        
        self.canvas = FigureCanvasTkAgg(self.figura, master=sezione_grafico)
        widget_canvas = self.canvas.get_tk_widget()
        widget_canvas.pack(fill=tk.BOTH, expand=True)
        
        self.figura.set_facecolor('#282c34')
        self.grafico.set_facecolor('#282c34')
        
        self.grafico.spines['top'].set_visible(False)
        self.grafico.spines['right'].set_visible(False)
        self.grafico.spines['left'].set_color('#abb2bf')
        self.grafico.spines['bottom'].set_color('#abb2bf')
        
        self.grafico.grid(True, linestyle='--', alpha=0.3, color='#abb2bf')
        
        self.grafico.set_xlabel('Quantità (q)', color='#abb2bf', fontsize=12)
        self.grafico.set_ylabel('Prezzo (p)', color='#abb2bf', fontsize=12)
        
        self.grafico.tick_params(colors='#abb2bf')
        
        self.grafico.set_title('Equilibrio di Mercato', color='#abb2bf', fontsize=14, pad=20)
        
        self.canvas.draw()
        
    def crea_sezione_risultati(self, genitore):
        sezione_risultati = ttk.LabelFrame(
            genitore, 
            text="Risultati", 
            style="Custom.TLabelframe",
            padding="20"
        )
        sezione_risultati.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        
        self.label_stato = ttk.Label(sezione_risultati, text="Stato: In attesa del calcolo", style="Custom.TLabel")
        self.label_stato.pack(anchor='w', pady=5)
        
        self.label_eq_offerta = ttk.Label(sezione_risultati, text="Equazione di Offerta: -", style="Custom.TLabel")
        self.label_eq_offerta.pack(anchor='w', pady=2)
        
        self.label_eq_domanda = ttk.Label(sezione_risultati, text="Equazione di Domanda: -", style="Custom.TLabel")
        self.label_eq_domanda.pack(anchor='w', pady=2)
        
        ttk.Separator(sezione_risultati, orient='horizontal', style="Custom.TSeparator").pack(fill='x', pady=10)
        
        self.label_quantita = ttk.Label(sezione_risultati, text="Quantità di equilibrio: -", style="Custom.TLabel")
        self.label_quantita.pack(anchor='w', pady=2)
        
        self.label_prezzo = ttk.Label(sezione_risultati, text="Prezzo di equilibrio: -", style="Custom.TLabel")
        self.label_prezzo.pack(anchor='w', pady=2)

    def calcola_equilibrio(self):
        try:
            a = float(self.campo_a.get())
            b = float(self.campo_b.get())
            c = float(self.campo_c.get())
            d = float(self.campo_d.get())
        except ValueError:
            messagebox.showerror("Errore", "Inserisci numeri validi per tutti i coefficienti.")
            return

        def offerta(q):
            return a * q**2 + b

        def domanda(p):
            return c - d * p

        def trova_equilibrio(a, b, c, d):
            valori_q = np.linspace(0, c*2, 1000)
            for q in valori_q:
                p = offerta(q)
                q_domanda = domanda(p)
                if np.isclose(q, q_domanda, atol=0.1):
                    return q, p
            return None, None

        q_eq, p_eq = trova_equilibrio(a, b, c, d)

        valori_q = np.linspace(0, c, 400)
        p_offerta = offerta(valori_q)
        q_domanda = domanda(p_offerta)

        self.grafico.clear()
        
        self.grafico.set_facecolor('#282c34')
        self.grafico.spines['top'].set_visible(False)
        self.grafico.spines['right'].set_visible(False)
        self.grafico.spines['left'].set_color('#abb2bf')
        self.grafico.spines['bottom'].set_color('#abb2bf')
        self.grafico.tick_params(colors='#abb2bf')
        
        self.grafico.plot(valori_q, p_offerta, label='Curva di Offerta', 
                         color='#61afef', linewidth=3, alpha=0.8)
        self.grafico.plot(q_domanda, p_offerta, label='Curva di Domanda', 
                         color='#e06c75', linewidth=3, alpha=0.8)
        
        if q_eq is not None and p_eq is not None:
            self.grafico.scatter(q_eq, p_eq, color='#98c379', s=150, zorder=5, 
                               edgecolors='white', linewidth=2)
            
            self.grafico.annotate(f'Equilibrio\nq={q_eq:.2f}\np={p_eq:.2f}', 
                                xy=(q_eq, p_eq), 
                                xytext=(20, 20),
                                textcoords='offset points',
                                bbox=dict(facecolor='#21252b', 
                                        edgecolor='#98c379', 
                                        alpha=0.9,
                                        boxstyle='round,pad=0.8'),
                                color='#abb2bf',
                                fontsize=10,
                                ha='left')
            
            self.label_eq_offerta.config(text=f"Equazione di Offerta: p = {a:.2f}q² + {b:.2f}")
            self.label_eq_domanda.config(text=f"Equazione di Domanda: q = {c:.2f} - {d:.2f}p")
            self.label_quantita.config(text=f"Quantità di equilibrio: {q_eq:.2f}")
            self.label_prezzo.config(text=f"Prezzo di equilibrio: {p_eq:.2f}")
            self.label_stato.config(text="Stato: Equilibrio trovato!", style="Success.TLabel")
        else:
            self.label_quantita.config(text="Quantità di equilibrio: Non trovato")
            self.label_prezzo.config(text="Prezzo di equilibrio: Non trovato")
            self.label_stato.config(text="Stato: Nessun equilibrio trovato", style="Error.TLabel")
            self.label_eq_offerta.config(text="Equazione di Offerta: -")
            self.label_eq_domanda.config(text="Equazione di Domanda: -")
        
        self.grafico.set_title('Equilibrio di Mercato', color='#abb2bf', fontsize=14, pad=20)
        self.grafico.set_xlabel('Quantità (q)', color='#abb2bf', fontsize=12)
        self.grafico.set_ylabel('Prezzo (p)', color='#abb2bf', fontsize=12)
        
        self.grafico.axhline(0, color='#abb2bf', linewidth=0.8, alpha=0.5)
        self.grafico.axvline(0, color='#abb2bf', linewidth=0.8, alpha=0.5)
        
        self.grafico.grid(True, linestyle='--', alpha=0.3, color='#abb2bf')
        
        legend = self.grafico.legend(facecolor='#21252b', edgecolor='#61afef', 
                                   labelcolor='#abb2bf', framealpha=0.9)
        legend.get_frame().set_linewidth(1)
        
        self.canvas.draw()

    def avvia(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = CalcolatoreEquilibrioMercato()
    app.avvia()