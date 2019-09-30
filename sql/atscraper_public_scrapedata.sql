create table scrapedata
(
	created_at varchar(225),
	date varchar(225),
	feedbacks text,
	header varchar(225),
	id bigint default nextval('increment'::regclass) not null
		constraint scrapedata_pkey
			primary key,
	keywords text,
	sub_header varchar(225),
	corp_id text,
	url varchar(225),
	website varchar(225),
	writer_email varchar(225),
	writer_name varchar(225),
	updated_at timestamp,
	sec_id varchar(225),
	time varchar(225),
	ck_feedback varchar(225) default 0
)
;
INSERT INTO public.scrapedata (created_at, date, feedbacks, header, id, keywords, sub_header, corp_id, url, website, writer_email, writer_name, updated_at, sec_id, time, ck_feedback) VALUES (null, null, '0', null, 1, null, null, null, 'collage', 'crop.com', null, null, null, null, null, '1');
INSERT INTO public.scrapedata (created_at, date, feedbacks, header, id, keywords, sub_header, corp_id, url, website, writer_email, writer_name, updated_at, sec_id, time, ck_feedback) VALUES ('2019-8-21 17:37:6', '25/08/2019', '0', 'מכשיר חדש בבורסה: רשות ני"ע שוקלת להנפיק אג"ח היברידי', 2659, null, 'מהן אגרות חוב היברידיות? איך זה שהן מהוות 3.5% מהיקפו של שוק האג"ח באירופה, ובמה יהיו שונות האגרות ההיברידיות בארץ מהאגרות בחו"ל?', null, 'https://www.bizportal.co.il/shukhahon/messRss2.xml', 'www.bizportal.co.il', null, 'ארז ליבנה ', null, '0', '18:01', '1');