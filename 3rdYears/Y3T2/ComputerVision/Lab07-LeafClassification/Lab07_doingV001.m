% Train Part
train_file = 'D:\AB-BiMaGOoOD\Tob-taun\3rdYears\Y3T2\ComputerVision\Lab07-LeafClassification\trainset\';
imageFiles = dir(fullfile(train_file, '*.jpg')); % List all JPG files
numImages = numel(imageFiles);

feature_vector_train = [];

for i = 1:numImages
    % Construct the full file path
    imgPath = fullfile(train_file, imageFiles(i).name); 
    img = imread(imgPath); % Read the image using the full path

    % Step 01: Shape Extraction
    gray_image = rgb2gray(img);

    shadding_pattern = imgaussfilt(gray_image, 195);
    h = double(shadding_pattern);
    g = double(gray_image);
    f = g ./ h;

    level = graythresh(f);
    disp(level);
    BW = imbinarize(f, level);
    BW = ~BW;

    % Use imfill for patch hole for post-processing
    BW_fill = imfill(BW, "holes");

    % Step 02: Feature Extraction
    STATS = regionprops(BW_fill, "Circularity");

    feature_vector_train(i, 1) = STATS.Circularity;
end

% Test Part
test_file = 'D:\AB-BiMaGOoOD\Tob-taun\3rdYears\Y3T2\ComputerVision\Lab07-LeafClassification\testset\';
imageFiles_test = dir(fullfile(test_file, '*.jpg')); % List all JPG files
numImages = numel(imageFiles_test);

feature_vector_test = [];

for i = 1:numImages
    % Construct the full file path
    imgPath = fullfile(test_file, imageFiles_test(i).name); 
    img = imread(imgPath); % Read the image using the full path

    % Step 01: Shape Extraction
    gray_image = rgb2gray(img);

    shadding_pattern = imgaussfilt(gray_image, 195);
    h = double(shadding_pattern);
    g = double(gray_image);
    f = g ./ h;

    level = graythresh(f);
    disp(level);
    BW = imbinarize(f, level);
    BW = ~BW;

    % Use imfill for patch hole for post-processing
    BW_fill = imfill(BW, "holes");

    % Step 02: Feature Extraction
    STATS = regionprops(BW_fill, "Circularity");

    feature_vector_test(i, 1) = STATS.Circularity;
end

% Step03: Classification
% 3.1 Train a multiclass ECOC model using the default options.
load('trainLabel.mat');
Mdl = fitcecoc(feature_vector_train,trainLabel);
% 3.2 Prediction
load('testLabel.mat');
predictedLabels = predict(Mdl,feature_vector_test);
table(testLabel(:),predictedLabels (:),'VariableNames',{'TrueLabels','PredictedLabels'})



