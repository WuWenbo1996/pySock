USE cabletemp;

DROP TABLE IF EXISTS data_result;

CREATE TABLE  data_result
(
    id       INT             NOT NULL    AUTO_INCREMENT  PRIMARY KEY,
    data     VARCHAR (1024)  NOT NULL,
    Created  DATETIME        NOT NULL
);

commit;