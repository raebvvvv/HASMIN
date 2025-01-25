<?php
include ('conn.php');
?>

<!doctype html> 
<html>
<head>
    <title>Register</title>
</head>

<body>
    <form action="">
    student number: <input type="text" name="student_number" required><br>
    password: <input type="password" name="password" required><br>
    name: <input type="text" name="name" required><br>
    email: <input type="email" name="email" required><br>
    <input type="file" id="image" name="image" required><br>
    <input type="submit" value="Register">

    </form>
    