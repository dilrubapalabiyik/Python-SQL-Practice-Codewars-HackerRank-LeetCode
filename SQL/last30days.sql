Select user_id sum(* case when 
'''
order amount for the last 30 days
'''

Date between  dateadd(day,-30,Date) and getDate() end as  tr 
group by user_id
 from orders;