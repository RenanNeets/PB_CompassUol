
CREATE TABLE Dim_Carro(
	id INTEGER PRIMARY KEY,
	km INTEGER,
	classi VARCHAR(50),
	marca VARCHAR(80),
	modelo VARCHAR(80),
	ano INTEGER,
	idCombustivel INTEGER,
	tipoCombustivel VARCHAR(20)
);

INSERT INTO Dim_Carro (km, classi, marca, modelo, ano, idCombustivel, tipoCombustivel)
SELECT ca.kmCarro, ca.classiCarro, ca.marcaCarro,ca.modeloCarro, ca.anoCarro, co.idCombustivel, co.tipoCombustivel 
FROM Carro ca 
JOIN Combustivel co ON co.idCombustivel = ca.idCombustivel 
GROUP BY ca.classiCarro 
ORDER BY ca.idCarro 
  
   
CREATE TABLE Dim_Cliente(
	id INTEGER PRIMARY KEY,
	nome VARCHAR(100),
	cidade VARCHAR(40),
	estado VARCHAR(40),
	pais VARCHAR(40)
);

INSERT INTO Dim_Cliente (id, nome, cidade, estado, pais)
SELECT cl.idCliente, cl.nomeCliente, cl.cidadeCliente, cl.estadoCliente, cl.paisCliente
FROM Cliente cl
GROUP BY cl.idCliente;
   
   
CREATE TABLE Dim_Vendedor (
	id INTEGER PRIMARY KEY,
	nome VARCHAR(15),
	sexo SMALLINT,
	estado VARCHAR(40)
); 

INSERT INTO Dim_Vendedor (id,nome,sexo,estado)
SELECT v.idVendedor, v.nomeVendedor, v.sexoVendedor, v.estadoVendedor 
FROM Vendedor v 
GROUP BY v.idVendedor 
   
CREATE TABLE Fato_Locacao(
	idCliente INTEGER NOT NULL,
	idCarro INTEGER NOT NULL,
	idVendedor INTEGER NOT NULL,
	data DATE,
	hora TIME,
	qtdDiaria INTEGER,
	vlrDiaria DECIMAL(10,2),
	dataEntrega DATE,
	horaEntrega TIME,
	FOREIGN KEY (idCliente) REFERENCES Dim_Cliente(id),
	FOREIGN KEY (idCarro) REFERENCES Dim_Carro(id),
	FOREIGN KEY (idVendedor) REFERENCES Dim_Vendedor(id)
);

INSERT INTO Fato_Locacao (idCliente,idCarro,idVendedor,data,hora,qtdDiaria,vlrDiaria,dataEntrega,horaEntrega)
SELECT  l.dataLocacao, l.horaLocacao, l.qtdDiaria, l.vlrDiaria, l.dataEntrega, l.horaEntrega, l.idCliente, l.idCarro, l.idVendedor
FROM Locacao l


SELECT * FROM Fato_Locacao
SELECT * FROM Dim_Vendedor dv 
SELECT * FROM Dim_Cliente 
SELECT * FROM Dim_Carro;