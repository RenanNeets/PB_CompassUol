CREATE TABLE Cliente (
	idCliente INTEGER PRIMARY KEY,
	nomeCliente VARCHAR(100),
	cidadeCliente VARCHAR(40),
	estadoCliente VARCHAR(40),
	paisCliente VARCHAR(40)
);
INSERT INTO Cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT tl.idCliente, tl.nomeCliente, tl.cidadeCliente, tl.estadoCliente, tl.paisCliente
FROM tb_locacao tl
GROUP BY tl.idCliente;




CREATE TABLE Combustivel AS
SELECT tl.idcombustivel, tl.tipoCombustivel
FROM tb_locacao tl 
GROUP BY tl.idcombustivel 




CREATE TABLE Carro (
	idCarro INTEGER PRIMARY KEY,
	kmCarro INTEGER,
	classiCarro VARCHAR(50),
	marcaCarro VARCHAR(80),
	modeloCarro VARCHAR(80),
	anoCarro INTEGER,
	idCombustivel INTEGER NOT NULL,
	FOREIGN KEY (idCombustivel) REFERENCES Combustivel(idCombustivel)
);

INSERT INTO Carro (kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel )
SELECT tl.kmCarro, tl.classiCarro, tl.marcaCarro, tl.modeloCarro, tl.anoCarro, tl.idcombustivel 
FROM tb_locacao tl 
GROUP BY tl.classiCarro 
ORDER BY tl.idLocacao 


CREATE TABLE Vendedor AS
SELECT tl.idVendedor, tl.nomeVendedor, tl.sexoVendedor, tl.estadoVendedor 
FROM tb_locacao tl 
GROUP BY tl.idVendedor 


CREATE TABLE Locacao(
	idLocacao INTEGER PRIMARY KEY,
	dataLocacao DATE,
	horaLocacao TIME,
	qtdDiaria INTEGER,
	vlrDiaria DECIMAL(10,2),
	dataEntrega DATE,
	horaEntrega TIME,
	idCliente INTEGER NOT NULL,
	idCarro INTEGER NOT NULL,
	idVendedor INTEGER NOT NULL,
	FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente),
	FOREIGN KEY (idCarro) REFERENCES Carro(idCarro),
	FOREIGN KEY (idVendedor) REFERENCES Vendedor(idVendedor)
);

INSERT INTO Locacao (idLocacao,dataLocacao,horaLocacao,qtdDiaria,vlrDiaria,dataEntrega,horaEntrega,idCliente,idCarro,idVendedor)
SELECT tl.idLocacao, tl.dataLocacao, tl.horaLocacao, tl.qtdDiaria, tl.vlrDiaria, tl.dataEntrega, tl.horaEntrega, tl.idCliente, tl.idCarro, tl.idVendedor
FROM tb_locacao tl

DROP TABLE tb_locacao 
