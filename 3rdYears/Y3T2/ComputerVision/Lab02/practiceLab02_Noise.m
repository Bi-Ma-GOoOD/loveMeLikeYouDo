picture = imread("D:\\AB-BiMaGOoOD\\Tob-taun\\3rdYears\\Y3T2\\ComputerVision\\Lab02\\lab2-noise averaging");
picture = zeros(size(picture));

picture_noise = 300;

for i = 1:300
    filename = ['D:\\AB-BiMaGOoOD\\Tob-taun\\3rdYears\\Y3T2\\ComputerVision\\Lab02\\lab2-noise averaging\\' num2str(i) '.jpg'];
    im = imread(filename);
    picture = picture + im;
end