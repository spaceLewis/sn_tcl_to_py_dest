

package cmd_sql

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Scanner;

public class SQLCommands {
    private Connection conn;

    public SQLCommands(String dbUrl, String username, String password) {
        try {
            conn = DriverManager.getConnection(dbUrl, username, password);
        } catch (SQLException e) {
            System.out.println("Error connecting to database: " + e.getMessage());
        }
    }

    public void createTable(String tableName, String columns) {
        String query = "CREATE TABLE IF NOT EXISTS " + tableName + " (" + columns + ")";
        try (PreparedStatement pstmt = conn.prepareStatement(query)) {
            pstmt.executeUpdate();
        } catch (SQLException e) {
            System.out.println("Error creating table: " + e.getMessage());
        }
    }

    public void insertData(String tableName, String data) {
        String query = "INSERT INTO " + tableName + " VALUES (" + data + ")";
        try (PreparedStatement pstmt = conn.prepareStatement(query)) {
            pstmt.executeUpdate();
        } catch (SQLException e) {
            System.out.println("Error inserting data: " + e.getMessage());
        }
    }

    public void selectData(String tableName) {
        String query = "SELECT * FROM " + tableName;
        try (PreparedStatement pstmt = conn.prepareStatement(query);
             ResultSet rs = pstmt.executeQuery()) {
            while (rs.next()) {
                System.out.println(rs.getString(1) + " " + rs.getString(2) + " " + rs.getString(3));
            }
        } catch (SQLException e) {
            System.out.println("Error selecting data: " + e.getMessage());
        }
    }

    public void updateData(String tableName, String column, String value, String condition) {
        String query = "UPDATE " + tableName + " SET " + column + " = '" + value + "' WHERE " + condition;
        try (PreparedStatement pstmt = conn.prepareStatement(query)) {
            pstmt.executeUpdate();
        } catch (SQLException e) {
            System.out.println("Error updating data: " + e.getMessage());
        }
    }

    public void deleteData(String tableName, String condition) {
        String query = "DELETE FROM " + tableName + " WHERE " + condition;
        try (PreparedStatement pstmt = conn.prepareStatement(query)) {
            pstmt.executeUpdate();
        } catch (SQLException e) {
            System.out.println("Error deleting data: " + e.getMessage());
        }
    }

    public void dropTable(String tableName) {
        String query = "DROP TABLE IF EXISTS " + tableName;
        try (PreparedStatement pstmt = conn.prepareStatement(query)) {
            pstmt.executeUpdate();
        } catch (SQLException e) {
            System.out.println("Error dropping table: " + e.getMessage());
        }
    }

    public void closeConnection() {
        try {
            conn.close();
        } catch (SQLException e) {
            System.out.println("Error closing connection: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter database URL:");
        String dbUrl = scanner.nextLine();
        System.out.println("Enter username:");
        String username = scanner.nextLine();
        System.out.println("Enter password:");
        String password = scanner.nextLine();

        SQLCommands sqlCommands = new SQLCommands(dbUrl, username, password);

        System.out.println("Enter table name:");
        String tableName = scanner.nextLine();
        System.out.println("Enter columns:");
        String columns = scanner.nextLine();
        sqlCommands.createTable(tableName, columns);

        System.out.println("Enter data:");
        String data = scanner.nextLine();
        sqlCommands.insertData(tableName, data);

        sqlCommands.selectData(tableName);

        System.out.println("Enter column:");
        String column = scanner.nextLine();
        System.out.println("Enter value:");
        String value = scanner.nextLine();
        System.out.println("Enter condition:");
        String condition = scanner.nextLine();
        sqlCommands.updateData(tableName, column, value, condition);

        sqlCommands.deleteData(tableName, condition);

        sqlCommands.dropTable(tableName);

        sqlCommands.closeConnection();
    }
}