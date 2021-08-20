Sub A_LDV_Format()
'
'Macro created by Neal
'
'''create worksheet2
    For Each ws In Worksheets
        If ws.Name = "sheet2" Then
        Sheets("sheet2").Delete
        End If
    Next



    Sheets.Add After:=Sheets(Sheets.Count)
    ActiveSheet.Name = "sheet2"


    Worksheets("Sheet1").Activate
    ActiveSheet.UsedRange.Select

    Selection.Copy

    Worksheets("sheet2").Activate
    Range("A1").Select
    ActiveSheet.Paste



'''''
    ActiveSheet.UsedRange.AutoFilter Field:=17, Criteria1:="good"
    ActiveSheet.UsedRange.Select
    With Selection.Interior
      .Pattern = xlSolid
        .PatternColorIndex = xlAutomatic
        .ThemeColor = xlThemeColorAccent3
        .TintAndShade = 0.399975585192419
        .PatternTintAndShade = 0
    End With
    ActiveSheet.UsedRange.AutoFilter Field:=17


    Range("A1:Q1").Select
    Selection.AutoFilter
    Columns("C:C").Select
    Selection.NumberFormat = "yyyy-mm-dd;@"
    Columns("E:E").Select
    Selection.NumberFormat = "$#,##0.00"
    Columns("M:P").Select
    Selection.NumberFormat = "$#,##0.00"
    Range("M55").Select
    Range("E1").Select
    Range(Selection, Selection.End(xlDown)).Select
    With Selection.Interior
        .Pattern = xlSolid
        .PatternColorIndex = xlAutomatic
        .ThemeColor = xlThemeColorAccent1
        .TintAndShade = 0.599993896298105
        .PatternTintAndShade = 0
    End With

    Range("O1:P1").Select
    Range(Selection, Selection.End(xlDown)).Select
    With Selection.Interior
        .Pattern = xlSolid
        .PatternColorIndex = xlAutomatic
        .ThemeColor = xlThemeColorAccent1
        .TintAndShade = 0.599993896298105
        .PatternTintAndShade = 0
    End With

    Columns("A:Q").EntireColumn.AutoFit


    '''

    ActiveSheet.UsedRange.AutoFilter Field:=17, Criteria1:="NO"
    ActiveSheet.UsedRange.Select
    With Selection.Interior
        .Pattern = xlSolid
        .PatternColorIndex = xlAutomatic
        .color = 65535
        .TintAndShade = 0
        .PatternTintAndShade = 0
    End With
    ActiveSheet.UsedRange.AutoFilter Field:=17
    ''
    Rows("2:2").Select

    ActiveWindow.FreezePanes = True
    Columns("A:Q").EntireColumn.AutoFit

End Sub