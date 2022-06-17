Public Class Form1
    Dim x, y, z As Double
    Dim znak As Integer

    Private Sub Two_Click(sender As Object, e As EventArgs) Handles Two.Click
        LabelAns.Text = LabelAns.Text + "2"
    End Sub

    Private Sub Three_Click(sender As Object, e As EventArgs) Handles Three.Click
        LabelAns.Text = LabelAns.Text + "3"
    End Sub

    Private Sub Four_Click(sender As Object, e As EventArgs) Handles Four.Click
        LabelAns.Text = LabelAns.Text + "4"
    End Sub

    Private Sub Five_Click(sender As Object, e As EventArgs) Handles Five.Click
        LabelAns.Text = LabelAns.Text + "5"
    End Sub

    Private Sub Six_Click(sender As Object, e As EventArgs) Handles Six.Click
        LabelAns.Text = LabelAns.Text + "6"
    End Sub

    Private Sub Seven_Click(sender As Object, e As EventArgs) Handles Seven.Click
        LabelAns.Text = LabelAns.Text + "7"
    End Sub

    Private Sub Eight_Click(sender As Object, e As EventArgs) Handles Eight.Click
        LabelAns.Text = LabelAns.Text + "8"
    End Sub

    Private Sub Nine_Click(sender As Object, e As EventArgs) Handles Nine.Click
        LabelAns.Text = LabelAns.Text + "9"
    End Sub

    Private Sub Drob_Click(sender As Object, e As EventArgs) Handles Drob.Click
        LabelAns.Text = LabelAns.Text + ","
    End Sub

    Private Sub Button3_Click(sender As Object, e As EventArgs) Handles Button3.Click
        x = LabelAns.Text
        LabelAns.Text = ""
        znak = 1
    End Sub

    Private Sub Button10_Click(sender As Object, e As EventArgs) Handles Button10.Click
        x = LabelAns.Text
        LabelAns.Text = ""
        znak = 2
    End Sub

    Private Sub Button15_Click(sender As Object, e As EventArgs) Handles Button15.Click
        x = LabelAns.Text
        LabelAns.Text = ""
        znak = 3
    End Sub

    Private Sub Delenie_Click(sender As Object, e As EventArgs) Handles Delenie.Click
        x = LabelAns.Text
        LabelAns.Text = ""
        znak = 4
    End Sub

    Private Sub AC_Click(sender As Object, e As EventArgs) Handles AC.Click
        x = 0
        y = 0
        z = 0
        znak = 0
        LabelAns.Text = ""
    End Sub

    Private Sub Result_Click(sender As Object, e As EventArgs) Handles Result.Click
        y = LabelAns.Text
        If znak = 1 Then z = x + y
        If znak = 2 Then z = x - y
        If znak = 3 Then z = x * y
        If znak = 4 Then z = x / y
        LabelAns.Text = z

    End Sub

    Private Sub One_Click(sender As Object, e As EventArgs) Handles One.Click
        LabelAns.Text = LabelAns.Text + "1"
    End Sub

    Private Sub Zero_Click(sender As Object, e As EventArgs) Handles Zero.Click
        LabelAns.Text = LabelAns.Text + "0"
    End Sub
End Class