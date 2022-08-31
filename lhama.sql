create table if not exists artist(
	id 			    integer primary key autoincrement,
	first_name	    text    not null,
	second_name     text,
	surname		    text,
	artist_id	    integer not null unique,
	link			text	not null unique,
	extraction_date	integer not null
);