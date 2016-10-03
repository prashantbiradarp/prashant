<script>
	$(document).ready(function()
		{
			$('#result_table').hide();
			$('#simple').submit
			(
				function(e)
				{
					e.preventDefault();

					$.ajax({
					type:'POST',
					url:'/user/compute/',
					data:{p:$('#principal').val(),
					r:$('#rate').val(),
					t:$('#time').val(),
					csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
					},
					success:function(data)
					{
					$('#result_table').show();
					$('#p').text(String(data.principal));
					$('#r').text(String(data.rate));
					$('#t').text(String(data.time));
					$('#result').text(String(data.result));
					return false;
					}
					
					});			
				});
		});
</script>