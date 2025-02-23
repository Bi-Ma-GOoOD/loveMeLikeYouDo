%% Training
load('trainLabel.mat');

numTrain = length(trainLabel);
featureMatrix = zeros(numTrain, 7); 

for i = 1:numTrain
    filename = ['D:\AB-BiMaGOoOD\Tob-taun\3rdYears\Y3T2\ComputerVision\Lab07-LeafClassification\trainset\' num2str(i) '.jpg'];
    im = imread(filename);
    grayImage = rgb2gray(im);

    shadePattern = imboxfilt(grayImage, 5555); 
    shadePattern_d = double(shadePattern);
    grayImage_d = double(grayImage);
    outpic = grayImage_d ./ shadePattern_d;

    gauss_im = imgaussfilt(outpic, 9);
    level = graythresh(gauss_im);
    bw = ~imbinarize(gauss_im, level);
    bw = imfill(bw, 'holes');

    stats = regionprops(bw, 'Perimeter', 'Area', 'Eccentricity', 'MajorAxisLength', 'MinorAxisLength', 'Orientation', 'Solidity');
    
    if ~isempty(stats)
        featureVector = [stats(1).Perimeter, stats(1).Area, stats(1).Eccentricity, ...
                         stats(1).MajorAxisLength, stats(1).MinorAxisLength, stats(1).Orientation, stats(1).Solidity];
    else
        featureVector = zeros(1, 7);
    end
    
    featureMatrix(i, :) = featureVector;
end

medianFeature = median(featureMatrix, 1);
madFeature = mad(featureMatrix, 1);
featureMatrix = (featureMatrix - medianFeature) ./ madFeature; 
%% Training Model
Mdl = fitcecoc(featureMatrix, trainLabel);
%% Test
load('testLabel.mat');

numTest = length(testLabel);
featureMatrix_test = zeros(numTest, 7);

for i = 1:numTest
    filename_test = ['D:\AB-BiMaGOoOD\Tob-taun\3rdYears\Y3T2\ComputerVision\Lab07-LeafClassification\testset\' num2str(i) '.jpg'];
    im_test = imread(filename_test);
    grayImage_test = rgb2gray(im_test);

    shadePattern_test = imboxfilt(grayImage_test, 5555); 
    shadePattern_d_test = double(shadePattern_test);
    grayImage_d_test = double(grayImage_test);
    outpic_test = grayImage_d_test ./ shadePattern_d_test;

    gauss_im_test = imgaussfilt(outpic_test, 9);
    level_test = graythresh(gauss_im_test);
    bw_test = ~imbinarize(gauss_im_test, level_test);
    bw_test = imfill(bw_test, 'holes');

    stats_test = regionprops(bw_test, 'Perimeter', 'Area', 'Eccentricity', 'MajorAxisLength', 'MinorAxisLength', 'Orientation', 'Solidity');
    
    if ~isempty(stats_test)
        featureVector_test = [stats_test(1).Perimeter, stats_test(1).Area, stats_test(1).Eccentricity, ...
                              stats_test(1).MajorAxisLength, stats_test(1).MinorAxisLength, stats_test(1).Orientation, stats_test(1).Solidity];
    else
        featureVector_test = zeros(1, 7);
    end
    
    featureMatrix_test(i, :) = featureVector_test;
end

featureMatrix_test = (featureMatrix_test - medianFeature) ./ madFeature; % Changed normalization method

%% Evaluate
predictedLabels = predict(Mdl, featureMatrix_test);
%% Result
resultsTable = table(testLabel(:), predictedLabels(:), 'VariableNames', {'TrueLabels', 'PredictedLabels'});
disp(resultsTable);

%% Confusion Matrix
figure(1);
cm = confusionchart(testLabel, predictedLabels);
cm.Title = 'Confusion Matrix - Leaf Classification';