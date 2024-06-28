// password-protect.js
function checkPassword() {
    var password = prompt("请输入密码:");
    if (password !== "lx051607") {
        alert("密码错误，访问被拒绝。");
        window.location.href = "access-denied.html";
    }
}

document.addEventListener("DOMContentLoaded", function() {
    if (window.location.pathname.endsWith("杂项&思考/随便写写/各种message的草稿/")) {
        checkPassword();
    }
});
