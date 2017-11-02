/**
 * Created by J on 2017/10/20.
 */


'use strict'

// 初始化simditor的函数
$(function() {
	var editor,toolbar;
	toolbar = ['title', 'bold', 'italic', 'underline', 'strikethrough', 'fontScale', 'color', '|', 'ol', 'ul', 'blockquote', 'code', 'table', '|', 'link', 'image', 'hr', '|', 'indent', 'outdent', 'alignment'];
	Simditor.locale = 'zh-CN';
	editor = new Simditor({
		textarea: $('#simditor'),
		toolbar: toolbar,
		pasteImage: true
	});
	// 加到window上去,其他地方才能访问到editor这个变量
	window.editor = editor;
});

$(function(){
   var dialog = $('#category-modal');
    $('#category-btn').click(function(){
        dialog.modal('show');
    });
    $('#category-submit-btn').click(function(){
        var categoryInput = $('#category-input');
        var categoryName = categoryInput.val();
        myajax.post({
            'url':'/cms/add_category/',
            'data':{'categoryname':categoryName},
            'success':function(result){
                if(result['code'] == 200){
                    var data = result['data'];
                    var select = $('#category-select');
                    dialog.modal('hide');
                    var option = $('<option></option>');
                    option.attr('value', data['id']);
                    option.html(data['name']);
                    select.append(option);
                    select.children().last().attr('selected','selected').siblings().remove('selected');
                }else{

                }
            },
            'error':function(error){
                console.log(error);
            }
        });
    });
});
