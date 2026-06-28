-- Seleciona o banco de dados que vamos utilizar
USE streamflix;

-- 1. Visualização inicial: Exibe os primeiros dados para conferência
SELECT * FROM usuarios;

-- 2. Soma total de minutos assistidos: Visão macro do consumo
SELECT SUM(Minutos_Assistidos) as Total_Geral FROM usuarios;

-- 3. Resumo por Plano: Quantos usuários temos e quantos minutos geram no total
SELECT Plano, COUNT(*) as Total_Usuarios, SUM(Minutos_Assistidos) as Total_Minutos
FROM usuarios
GROUP BY Plano;

-- 4. Métricas de engajamento: Cálculo de média e máximo por plano (ordenado pelo maior engajamento)
SELECT 
    Plano, 
    COUNT(*) as Total_Usuarios, 
    ROUND(AVG(Minutos_Assistidos), 2) as Media_Minutos,
    MAX(Minutos_Assistidos) as Max_Minutos
FROM usuarios
GROUP BY Plano
ORDER BY Media_Minutos DESC;

-- 5. Filtro de alta performance: Seleciona usuários que superam o limite de 450 minutos
SELECT * FROM usuarios
WHERE Minutos_Assistidos > 450 
ORDER BY Minutos_Assistidos DESC;

-- 6. Análise Temporal: Quantos novos usuários entraram por data
SELECT 
    Data_Adesao, 
    COUNT(*) as Novos_Usuarios
FROM usuarios
GROUP BY Data_Adesao
ORDER BY Data_Adesao ASC;

-- 7. Subquery: Identifica usuários que assistiram acima da média geral de todo o Streamflix
SELECT * FROM usuarios 
WHERE Minutos_Assistidos > (SELECT AVG(Minutos_Assistidos) FROM usuarios);