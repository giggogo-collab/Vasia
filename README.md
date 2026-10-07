<Window x:Class="PracticalWork4.MainWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Title="Практическая работа №4 – Pair" Height="500" Width="600"
        ResizeMode="CanMinimize" WindowStartupLocation="CenterScreen"
        Icon="/icon.ico" FontSize="12">
    <Grid Margin="15">
        <Grid.RowDefinitions>
            <RowDefinition Height="Auto"/>
            <RowDefinition Height="Auto"/>
            <RowDefinition Height="*"/>
            <RowDefinition Height="Auto"/>
        </Grid.RowDefinitions>

        <!-- Первая пара -->
        <GroupBox Grid.Row="0" Header="Первая пара" Margin="0,0,0,10">
            <StackPanel Orientation="Horizontal" Margin="5">
                <Label Content="First:"/>
                <TextBox x:Name="tbFirst1" Width="60" Text="1"/>
                <Label Content="Second:" Margin="15,0,0,0"/>
                <TextBox x:Name="tbSecond1" Width="60" Text="2"/>
            </StackPanel>
        </GroupBox>

        <!-- Вторая пара -->
        <GroupBox Grid.Row="1" Header="Вторая пара" Margin="0,0,0,10">
            <StackPanel Orientation="Horizontal" Margin="5">
                <Label Content="First:"/>
                <TextBox x:Name="tbFirst2" Width="60" Text="3"/>
                <Label Content="Second:" Margin="15,0,0,0"/>
                <TextBox x:Name="tbSecond2" Width="60" Text="4"/>
            </StackPanel>
        </GroupBox>

        <!-- Результат -->
        <GroupBox Grid.Row="2" Header="Результат" Margin="0,0,0,10">
            <TextBox x:Name="tbResult" IsReadOnly="True" TextWrapping="Wrap"
                     VerticalScrollBarVisibility="Auto"/>
        </GroupBox>

        <!-- Кнопки -->
        <StackPanel Grid.Row="3" Orientation="Horizontal" HorizontalAlignment="Center">
            <Button x:Name="btnSumFields" Content="Сумма полей" Width="100" Margin="5" Click="btnSumFields_Click"/>
            <Button x:Name="btnAddPairs" Content="Сложить пары" Width="100" Margin="5" Click="btnAddPairs_Click"/>
            <Button x:Name="btnIncrease1" Content="Увеличить на 1" Width="100" Margin="5" Click="btnIncrease1_Click"/>
            <Button x:Name="btnSumThree" Content="Сложить 3 пары" Width="100" Margin="5" Click="btnSumThree_Click"/>
            <Button x:Name="btnAbout" Content="О программе" Width="100" Margin="5" Click="btnAbout_Click"/>
            <Button x:Name="btnExit" Content="Выход" Width="80" Margin="5" Click="btnExit_Click"/>
        </StackPanel>
    </Grid>
</Window>  . 
