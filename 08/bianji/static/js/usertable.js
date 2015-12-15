/**
 * Created by bianji on 15/12/15.
 */
      //页面加载查询
        $(document).ready(function() {
            $.get('/userlist',function(data) {
                for (var i=0;i<data.message.length;i++) {
                    var temp = '';
                    temp += '<tr><td>' + data.message[i][0] + '</td><td>' + data.message[i][1] + '</td><td><a class="delete">删除</a></td></tr>';
                    console.log(temp);
                    $("tbody").append(temp)
                }
            });
        });
        //添加
        $(function () {
            $("#adduser").on('submit',function(){
                $.post('/add',{
                    username:$('input[name="username"]').val(),
                    password:$('input[name="password"]').val()
                }).then(function(data) {
                if (data['code'] == 200) {
                        var temp = '';
                        temp += '<tr><td>' + $('input[name="username"]').val()+ '</td><td>' + $('input[name="password"]').val() + '</td><td><a class="delete">删除</a></td></tr>';
                        console.log(temp);
                        $('tbody').prepend(temp)
                }
            });
            return false
            });
        });
        //删除
       $(document).on('click','.delete',function() {
           var item = $(this).closest('tr');
           //$(item).remove();
           $username = item.children('td:first').html();
           $.post('/del',{
               username: $username
           },function(data) {
               if (data['code'] == 200) {
                   alert('删除成功');
                   $(item).remove();
               }
           })
       });