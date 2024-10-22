var cache_token = "";
var username = "";
if(localStorage.getItem("cache_token") != null) {
	cache_token = localStorage.getItem("cache_token");
}

if(cache_token == "") {
	layer.msg('检测到您未登录，正在跳转到登录页面');
	setTimeout(function() {
		location.href = "/views/login.html";
	}, 1000);
} else {
	$.ajax({
		url: "http://localhost:8080/token-verify/",
		type: "post",
		async: false,
		dataType: "json",
		data: {
			"token": cache_token
		},
		success: function(data) {
			username = data.username;
		},
		error: function(jqXHR) {
			localStorage.removeItem("cache_token");
			layui.layer.msg('检测到您未登录，正在跳转到登录页面');
			setTimeout(function() {
				location.href = "/views/login.html";
			}, 1000);
		}
	})
}

function get_username() {
	return username;
}