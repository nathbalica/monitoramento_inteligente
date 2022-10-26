-- create table public.mac_adress(
-- 	id_mac serial not null,
-- 	mac_number character varying(255) not null
-- )

-- ALTER TABLE ONLY public.mac_adress
--     ADD CONSTRAINT PK_mac_adress PRIMARY KEY (id_mac);

CREATE TABLE public.measurer_data (
	id_measurer serial not null,
    mac_name character varying(255) NOT NULL,
    date_measurer TIMESTAMP NOT NULL,
    rssi integer NOT NULL,
    va integer NOT NULL, 
    vb integer NOT NULL,
    vc integer NOT NULL,
    ia integer NOT NULL,
    ib integer NOT NULL,
    ic integer NOT NULL,
    wa integer NOT NULL,
    wb integer NOT NULL,
    wc integer NOT NULL
);

ALTER TABLE ONLY public.measurer_data
    ADD CONSTRAINT PK_measurer_data PRIMARY KEY (id_measurer);

-- ALTER TABLE ONLY public.measurer_data
--     ADD CONSTRAINT PK_measurer_data FOREIGN KEY (mac_name) references mac_adress (id_mac);

-- insert into measurer_data (mac_name, date, rssi, va, vb, vc, ia, ib, ic, wa, wb, wc)
-- values ('DE:DD:26:74:3D:70', '2022-10-26T17:35:56Z', -26, 204.12, 226.21, 219.99, 27.35, 10.01, 25.77, 5582.682000000001, 2264.3621,
-- 5669.1423);

-- delete from measurer_data ;

-- select * from measurer_data md ;