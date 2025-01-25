<?php
include ('conn.php');



?>
<!doctype html> 
<html>
<head>
    <title>Log In</title>
</head>     
<body>
    <h1>Log In</h1>
    <form action="login.php" method="post">
        <label for="username">Username:</label>
        <input type="text" name="username" id="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" name="password" id="password" required>
        <br>
        <input type="submit" value="Log In">Login</button>  
        <input type="submit" value="Sign up">Sign in</button> 
    </form>




<?php



    mysqli_close($conn);
?>