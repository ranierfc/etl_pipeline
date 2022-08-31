create table if not exists artist(
	id 			    integer primary key autoincrement,
	first_name	    text,
	second_name     text,
	surname		    text,
	artist_id	    integer,
	link			text,
	extraction_date	integer
);