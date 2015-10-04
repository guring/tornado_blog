# Markdown使用手册

* slug: Markdown使用手册
* published: 2014-07-28 23:41
* tags: Markdown, 随记
* category: 随记

----------------------------------------------------------

个人博客第一篇文章，用 Markdown 写的，尽管有点小麻烦，但慢慢就会熟悉起来的，这里把常用方法做一个总结。

### 一、首行缩进

在段首加入`&ensp;`来输入一个空格.加入`&emsp;` `&emsp;`来输入两个空格。

### 二、插入代码
 
* 在代码两侧加入一个反引号 `  （单行的）
* 在代码两侧添加三个反引号 ```  （多行的）
* 反引号最好在代码的前后行添加，而不是直接加在代码两边
* 添加空行可以结束先前的格式状态。建议在改变格式时，均添加一个空行。

### 三、列表

* 用 `*` 来代表无序列表
* 直接在文字前加1. 2. 3. `符号要和文字之间加上一个字符的空格`
* 如果列表项目间用空行分开，在输出 HTML 时 Markdown 就会将项目内容用 `<p>` 标签包起来
* 列表项目可以包含多个段落，每个项目下的段落都必须缩进 4 个空格或是 1 个制表符
* 如果要在列表项目内放进引用，那 `>` 就需要缩进
* 如果要放代码区块的话，该区块就需要缩进两次，也就是 8 个空格或是 2 个制表符

### 四、引用

在文本前加入 `>` 这种尖括号（大于号）

### 五、图片和链接

插入链接与插入图片的语法很像，区别在一个 !号。到目前为止， Markdown 还没有办法指定图片的宽高，如果你需要的话，你可以使用普通的 <img> 标签。

* 图片：`![]()`
* 链接：`[]()`  
 
**1、参考式链接：**

```
I get 10 times more traffic from [Google] [1] than from
[Yahoo] [2] or [MSN] [3].

  [1]: http://google.com/        "Google"
  [2]: http://search.yahoo.com/  "Yahoo Search"
  [3]: http://search.msn.com/    "MSN Search"
  ```
如果改成用链接名称的方式写：

```
I get 10 times more traffic from [Google][] than from
[Yahoo][] or [MSN][].

  [google]: http://google.com/        "Google"
  [yahoo]:  http://search.yahoo.com/  "Yahoo Search"
  [msn]:    http://search.msn.com/    "MSN Search"
```
**2、行内式链接：(不建议使用)**

```
I get 10 times more traffic from [Google](http://google.com/ "Google")
than from [Yahoo](http://search.yahoo.com/ "Yahoo Search") or
[MSN](http://search.msn.com/ "MSN Search").
```

### 六、粗体和斜体

* 用两个  `*`  包含一段文本就是粗体的语法，用一个 `*` 包含一段文本就是斜体的语法
* 如果你的 * 和 _ 两边都有空白的话，它们就只会被当成普通的符号
* 如果要在文字前后直接插入普通的星号或底线，你可以用反斜线

**注**： 建议用 `**` 表示粗体， `_` 表示斜体

### 七、分割线

用三个 `*` 或者 `_`来表示， 不过建议用一整行 `_` 来表示，易于辨识

### 八、插入表格

目前编辑器不支持表格，以往是通过截图，呈现的效果并不好，Markdown支持html，所以我们可以用html来写表格。但是......

用html写表格，实在太麻烦了，这里有个简单的转换方法，
参考[Markdown之表格的处理](http://pressbin.com/tools/excel_to_html_table/index.html)

### 九、兼容 HTML

HTML 是一种发布的格式，Markdown 是一种书写的格式。不在 Markdown 涵盖范围之内的标签，都可以直接在文档里面用 HTML 撰写。不需要额外标注这是 HTML 或是 Markdown；只要直接加标签就可以了。

要制约的只有一些 HTML 区块元素――比如 `<div>`、`<table>`、`<pre>`、`<p>` 等标签，必须在前后加上空行与其它内容区隔开，还要求它们的开始标签与结尾标签不能用制表符或空格来缩进。Markdown 的生成器有足够智能，不会在 HTML 区块标签外加上不必要的 `<p>` 标签。

例子如下，在 Markdown 文件里加上一段 HTML 表格：

```HTML
这是一个普通段落。
<table>
    <tr>
        <td>Foo</td>
    </tr>
</table>
这是另一个普通段落。
```

请注意，在 HTML 区块标签间的 Markdown 格式语法将不会被处理。比如，你在 HTML 区块内使用 Markdown 样式的`*强调*`会没有效果。

HTML 的区段（行内）标签如 `<span>`、`<cite>`、`<del>` 可以在 Markdown 的段落、列表或是标题里随意使用。依照个人习惯，甚至可以不用 Markdown 格式，而直接采用 HTML 标签来格式化。举例说明：如果比较喜欢 HTML 的 `<a>` 或 `<img>` 标签，可以直接使用这些标签，而不用 Markdown 提供的链接或是图像标签语法。

和处在 HTML 区块标签间不同，Markdown 语法在 HTML 区段标签间是有效的。

### 十、特殊字符自动转换 ###

在 HTML 文件中，有两个字符需要特殊处理： < 和 & 。 < 符号用于起始标签，& 符号则用于标记 HTML 实体，如果你只是想要显示这些字符的原型，你必须要使用实体的形式，像是 `&lt;` 和 `&amp;` 

`4 < 5` 

Markdown 将会把它转换为： 

`4 &lt; 5` 

不过需要注意的是，code 范围内，不论是行内还是区块， < 和 & 两个符号都一定会被转换成 HTML 实体，这项特性让你可以很容易地用 Markdown 写 HTML code （和 HTML 相对而言， HTML 语法中，你要把所有的 < 和 & 都转换为 HTML 实体，才能在 HTML 文件里面写出 HTML code。）

### 十一、换行

Markdown 允许段落内的强迫换行（插入换行符），如果你确实想要依赖 Markdown 来插入 `<br />` 标签的话，在插入处先按入两个以上的空格然后回车。

### 十二、反斜杠

Markdown 支持以下这些符号前面加上反斜杠来帮助插入普通的符号：

```
\   反斜线
`   反引号
*   星号
_   底线
{}  花括号
[]  方括号
()  括弧
#   井字号
+   加号
-   减号
.   英文句点
!   惊叹号
```

### 参考连接

* [Markdown 语法说明 (简体中文版)](http://wowubuntu.com/markdown/)