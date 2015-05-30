<!DOCTYPE html>
<html>
<head>
<title>Hello World!</title>
</head>
<body>
<p>
Welcome {{username}}
</p>
Some Fruits:
<ul>
%for thing in things:
<li>{{thing}}</li>
%end
</ul>
<form action="/favourite_fruit" method="POST">
<label>What is your favourite fruit?</label>
<input type="text" name="fruit" size="40" value=""><br>
<input type="submit" value="Submit">
</form>
</body>
</html>