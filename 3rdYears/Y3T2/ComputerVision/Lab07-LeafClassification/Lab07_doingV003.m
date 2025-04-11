outpicCollection = cell(25, 1);
processedImages = cell(25, 1);

outpicCollection_test = cell(15, 1);
processedImages_test = cell(15, 1);

load('trainLabel.mat');

numTrain = length(trainLabel);
featureMatrix = zeros(numTrain, 6);

for i = 1:numTrain
    filename = ['D:\AB-BiMaGOoOD\Tob-taun\3rdYears\Y3T2\ComputerVision\Lab07-LeafClassification\trainset\' num2str(i) '.jpg'];
    im = imread(filename);
    grayImage = rgb2gray(im);

    shadePattern = imboxfilt(grayImage, 2055);
    shadePattern_d = double(shadePattern);
    grayImage_d = double(grayImage);
    outpic = grayImage_d ./ shadePattern_d;

    gauss_im = imgaussfilt(outpic, 6);
    level = graythresh(gauss_im);
    % disp(level);
    bw = ~imbinarize(gauss_im, level);
    bw = imfill(bw, 'holes');

    stats = regionprops(bw, 'Perimeter', 'Area', 'Eccentricity', 'MajorAxisLength', 'MinorAxisLength', 'Orientation');
    
    if ~isempty(stats)
        featureVector = [stats.Perimeter, stats.Area, stats.Eccentricity, ...
                         stats.MajorAxisLength, stats.MinorAxisLength, stats.Orientation];
    else
        featureVector = zeros(1, 6);
    end

    outpicCollection{i} = featureVector;
    processedImages{i} = bw;
    
    featureMatrix(i, :) = featureVector;
end

meanFeature = mean(featureMatrix, 1);
stdFeature = std(featureMatrix, 1);
featureMatrix = (featureMatrix - meanFeature) ./ stdFeature;

Mdl = fitcecoc(featureMatrix, trainLabel);

load('testLabel.mat');

numTest = length(testLabel);
featureMatrix_test = zeros(numTest, 6);

for i = 1:numTest
    filename_test = ['D:\AB-BiMaGOoOD\Tob-taun\3rdYears\Y3T2\ComputerVision\Lab07-LeafClassification\testset\' num2str(i) '.jpg'];
    im_test = imread(filename_test);
    grayImage_test = rgb2gray(im_test);

    shadePattern_test = imboxfilt(grayImage_test, 5055);
    shadePattern_d_test = double(shadePattern_test);
    grayImage_d_test = double(grayImage_test);
    outpic_test = grayImage_d_test ./ shadePattern_d_test;

    gauss_im_test = imgaussfilt(outpic_test, 25);
    level_test = graythresh(gauss_im_test);
    % disp(level_test);
    bw_test = ~imbinarize(gauss_im_test, level_test);
    bw_test = imfill(bw_test, 'holes');

    stats_test = regionprops(bw_test, 'Perimeter', 'Area', 'Eccentricity', 'MajorAxisLength', 'MinorAxisLength', 'Orientation');

    if ~isempty(stats_test)
        featureVector_test = [stats_test.Perimeter, stats_test.Area, stats_test.Eccentricity, ...
                              stats_test.MajorAxisLength, stats_test.MinorAxisLength, stats_test.Orientation];
    else
        featureVector_test = zeros(1, 6);
    end

    outpicCollection_test{i} = featureVector_test;
    processedImages_test{i} = bw_test;
    
    featureMatrix_test(i, :) = featureVector_test;
end

featureMatrix_test = (featureMatrix_test - meanFeature) ./ stdFeature;

predictedLabels = predict(Mdl, featureMatrix_test);

resultsTable = table(testLabel(:), predictedLabels(:), 'VariableNames', {'TrueLabels', 'PredictedLabels'});
disp(resultsTable);

% Confusion Matrix
figure(3)
cm = confusionchart(testLabel, predictedLabels);