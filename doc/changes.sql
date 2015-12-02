-- encontrar duplicados (partes diarios que apuntan a un mismo registro de equipo
SELECT id, numero, fecha, operario, pd.equipo FROM partediario pd
INNER JOIN (SELECT equipo FROM partediario
GROUP BY equipo HAVING count(id) > 1) dup ON pd.equipo = dup.equipo