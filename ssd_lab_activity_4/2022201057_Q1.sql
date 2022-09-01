DELIMITER &&
CREATE PROCEDURE `addNums`(IN num1 int, IN num2 int, OUT sum int) 
BEGIN 
Set sum = num1 + num2; 
END&&
DELIMITER ;

CALL `addNums`(20,78,@sumNums);
SELECT @sumNums;
