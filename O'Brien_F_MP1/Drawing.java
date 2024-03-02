public class Drawing{

    public static char[][] printCanvas(char[][] arr){
        int numRows = arr.length;
        int numCols = arr[0].length;

        for (int i=0;i<numRows;++i){
           System.out.print(numRows - 1 -i); //print the Y axis number
           for(int j=0; j<numCols; ++j){
            System.out.print(arr[i][j]); //print out the array over each row
           }
           System.out.println();
        }
        System.out.print(' '); //print a space
        for (int k=0; k<numCols; ++k){
            System.out.print(k); //print the x axis number
        }

        return arr;

        }

    public static char[][] createCanvas(char[][] arr){
        int numRows = arr.length;
        int numCols = arr[0].length;

        for(int i=0;i<numRows;++i){
            for(int j=0;j<numCols;++j){ //assign every slot in the array as a space character
                arr[i][j] = ' ';


            }
        }

        for(int k=0;k<numCols;++k){
            arr[0][k] = '='; //assign every character in the first row to be an equal sign
        }
        for(int p=0;p<numCols;++p){
            arr[numRows -1][p] = '='; // assign every character in the last row to an equal sign
        }
        for(int q = 0; q<numRows -2;++q){ // assigning the remaining borders to '|'
            arr[q+1][0] = '|'; 
        }
        for(int r=0; r<numRows -2;++r){
            arr[r+1][numCols -1] = '|';
        }
        arr[0][0] = '+'; //assigning top left corner to a plus sign
        arr[0][numCols -1] = '+'; //assigning top right corner to a plus sign
        arr[numRows -1][0] = '+'; //assigning bottom left corner to a plus sign
        arr[numRows -1][numCols -1] = '+'; //assigning bottom right corner to a plus sign

        return arr;


    }

    public static char[][] addCharacter(char[][] arr, char z, int a, int b){
        int numRows = arr.length;
        arr[numRows - b - 1][a] = z; //puts character z at [a][b]

        return arr;
    }

    public static void main(String[] args){

        char[][] array1 = new char[5][10];

        Drawing.createCanvas(array1);

        Drawing.addCharacter(array1, '(', 4, 2);

        Drawing.addCharacter(array1, ':', 5, 2);

        Drawing.printCanvas(array1);


    }
    


    }

