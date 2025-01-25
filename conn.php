<?php
$username = "root";
$password = "";
$server = 'localhost';
$db = 'hasmin_db';

$conn = mysqli_connect($server, $username, $password, $db);

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

echo "Connected successfully to the database.";
?>