<?php
// 数据库连接信息
$servername = "localhost";
$username = "root";
$password = "root";
$dbname = "sqli_test";

// 创建数据库连接
$conn = new mysqli($servername, $username, $password, $dbname);

// 检查连接是否成功
if ($conn->connect_error) {
    die("Error: " . $conn->connect_error);
}

$username = $_GET['uname'];

// 查询数据库
$sql = "SELECT * FROM `users` WHERE username = '$username'";
echo $sql."<br>";
$result = $conn->query($sql);

if (!$result) {
    echo $conn->error."<br>";
}
if ($result->num_rows > 0) {
    // echo "<p>User Found</p>";
} else {
    // echo "<p>Not Found</p>";
}

// 关闭数据库连接
$conn->close();

?>
