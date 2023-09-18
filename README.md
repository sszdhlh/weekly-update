# weekly-update
update weekly data
## Problem：update weekly data
### Steps：
点击打开Cin7里面的网页，点击上方Sales Orders，选择从上周一到当天日期的Date，Date前面下选框选择”Created”,Stages那里选择除了”Awaiting Payment”和”Cancelled”的所有选项。
右面Sales Order Status选择”Search all”,等待页面刷新后，选择下面结果中左面的”Actions”,点击选择”Export Sales Orders Details”

跳转页面后，需要点击“Item BOM Load”和 invoice date的box，然后选中后，点击右上角的”Export Data”,跳转到确认导出页面后，再次点击”Export”，这样csv文件就成功导出并下载了。
将下载的csv文件复制到”各sku销量-Weekly”脚本”cin7 data”中，然后运行sales by sku.py文件，这样得到的结果salenum by sku.csv。可以在文件夹中进行复核。
复核的时候，点击打开salenum by sku.csv文件，选中”Number”这一列，然后进行排序和筛选功能中的排序，使用降序，看一下数量是否正确。看到第二个Display-BK中number为小数点，去查看，发现只是展示品，应该是自己填的数字，而不是系统生成的数字，那么就成功输出了结果文件。
