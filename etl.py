import pandas as pd

usuarios = pd.read_csv("usuarios.csv")

usuarios["mensagem"] = usuarios.apply(
    lambda row: f"Olá {row['nome']}, sua conta {row['conta']} está vinculada ao cartão {row['cartao']}.",
    axis=1
)

usuarios[["mensagem"]].to_csv("mensagens.csv", index=False)

print("✅ Processo ETL concluído! Mensagens salvas em 'mensagens.csv'.")
