cd ('D:\AB-BiMaGOoOD\Tob-taun\3rdYears\Y3T2\ComputerVision\Lab02\lab2-noise averaging\')
total = double(zeros(size(imread('puppy_1.jpg'))));
for i = 1:300
    filename = ['puppy_' , num2str(i),'.jpg'];
    im = imread(filename);
    im = double(im);
    total = total + im;
end
total = uint8(total / 300);
imshow(total)