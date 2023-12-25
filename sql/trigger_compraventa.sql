CREATE TRIGGER ReferenciaCatrastal BEFORE INSERT
ON Propiedad
FOR EACH ROW
IF NEW.Ref_catrastal > 0000 && NEW.Ref_catrastal < 9999 OR //eXISTE THEN
SIGNAL SQLSTATE '50001' SET MESSAGE_TEXT = 'Referencia catrastal no valido';
END IF


