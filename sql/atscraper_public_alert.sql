create table scrapeAlert
(
	created_at varchar(225),
	date varchar(225),
	feedbacks text,
	header varchar(225),
	id bigint default nextval('increment_3'::regclass) not null
		constraint scrapealert_pkey
			primary key,
	keyword text,
	sub_header text,
	corp_id text,
	url varchar(225),
	website varchar(225),
	writer_email varchar(225),
	writer_name varchar(225),
	updated_at timestamp,
	sec_id varchar(225),
	secId varchar(225),
	time varchar(225),
	ck_feedback varchar(225) default 0,
	status bigint default 0
)
;