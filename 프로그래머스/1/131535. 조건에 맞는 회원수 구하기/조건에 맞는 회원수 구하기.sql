-- 코드를 입력하세요
SELECT COUNT(AGE) AS USERS
FROM USER_INFO
WHERE AGE BETWEEN 20 and 29
and JOINED LIKE "2021%"