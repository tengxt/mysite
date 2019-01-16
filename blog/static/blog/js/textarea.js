$(function() {
    var editor = new Simditor({
        textarea: $("#id_content"),
        placeholder: "在此编辑你的文章",
        autosave: 'editor-content',
        toolbar: [
        'title', 'bold', 'italic', 'underline', 'strikethrough', 'fontScale', 'color',
        '|', 'code', 'link', 'image', 'blockquote',
        '|', 'hr', 'ul', 'ol', 'alignment', 'table',
        '|', 'html', 'markdown'
        ],
        codeLanguages: [
        { name: 'Python', value: 'python' },
        { name: 'Django', value: 'django' },
        { name: 'Shell', value: 'shell' },
        { name: 'Apache', value: 'apache' },
        { name: 'Java', value: 'java' },
        { name: 'CSS', value: 'css' },
        { name: 'JavaScript', value: 'javascript' },
        { name: 'HTML,XML', value: 'html' },
        { name: 'No Highlight', value: 'nohighlight' },
        { name: 'Diff', value: 'diff' },
        { name: 'SQL', value: 'sql' },
        { name: 'C++', value: 'c++' },
        { name: 'C#', value: 'cs' },
        { name: 'JSON', value: 'json' },
        { name: 'Markdown', value: 'markdown' },
        ]
    });
    $('#id_content').attr("data-autosave-confirm", "是否读取上次退出时未保存的草稿？");
});