-- This SQL have been developed using MariaDB as a source
select
	Request_at,
	FORMAT(sum(cancelled_count) / count(1), 2) Percentage_Of_Cancelled_Rides
from
	(
	select
		*,
		case
			when t.Status in ('cancelled_by_driver',
			'cancelled_by_client') then 1
			else 0
		end as cancelled_count
	from
		Trips t
	left join Users u on
		t.Client_Id = u.Users_Id
	where
		Banned = 'No'
		and t.Request_at BETWEEN '2013-10-01' and '2013-10-03') all_rides
group by
	all_rides.Request_at